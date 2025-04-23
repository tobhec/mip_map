let table = document.getElementById("table");

function toTable(text){
    if(!text || !table) {
        return;
    }

    while(table.lastElementChild){
        table.removeChild(table.lastElementChild);
    }

    let rows = text.split("\n");
    let headers = rows.shift().trim().split(",");
    let hTableRow = document.createElement("tr");

    headers.forEach(function(header) {
        let tableHeader = document.createElement("th");
        let trimmedHeader = header.trim();
        if(trimmedHeader) {
            tableHeader.textContent = trimmedHeader;
            hTableRow.appendChild(tableHeader);
        }
    });

    table.appendChild(hTableRow);
    rows.forEach(function(row){
        row = row.trim();
        if (!row) return;

        let cols = row.split(",");
        let rTableRow = document.createElement("tr");

        cols.forEach(function(cell){
            let tableCell = document.createElement("td");
            tableCell.textContent = cell.trim();
            rTableRow.appendChild(tableCell);
        });

        table.appendChild(rTableRow);
    });
}

function extractByYearAndIndicator(targetYear, targetIndicator) {
    const rows = table.querySelectorAll("tr");
    if (rows.length < 2) return {};

    const headers = Array.from(rows[0].querySelectorAll("th")).map(th => th.textContent.trim());

    const yearIndex = headers.indexOf("Year");
    const countryIndex = headers.indexOf("Country");
    const valueIndex = headers.indexOf("Value");
    const indicatorIndex = headers.indexOf("Indicator");

    if ([yearIndex, countryIndex, valueIndex, indicatorIndex].includes(-1)) return {};

    const result = {};
    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].querySelectorAll("td");
        const year = cells[yearIndex]?.textContent.trim();
        const indicator = cells[indicatorIndex]?.textContent.trim();
        const country = cells[countryIndex]?.textContent.trim();
        const value = cells[valueIndex]?.textContent.trim();

        if (year === targetYear && indicator === targetIndicator && country && value) {
            result[country] = isNaN(value) ? value : parseFloat(value);
        }
    }
    return result;
}

function populateDropdowns(rows, headers) {
    const yearDropdown = document.getElementById("yearDropdown");
    const indicatorDropdown = document.getElementById("indicatorDropdown");

    const yearSet = new Set();
    const indicatorSet = new Set();

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].querySelectorAll("td");
        const year = cells[headers.indexOf("Year")]?.textContent.trim();
        const indicator = cells[headers.indexOf("Indicator")]?.textContent.trim();

        if (year) yearSet.add(year);
        if (indicator) indicatorSet.add(indicator);
    }

    // Convert sets to arrays so we can pick the first one
    const yearArray = Array.from(yearSet).sort();
    const indicatorArray = Array.from(indicatorSet).sort();

    // Fill dropdowns with options
    yearArray.forEach(year => {
        let option = document.createElement("option");
        option.value = year;
        option.textContent = year;
        yearDropdown.appendChild(option);
    });
    indicatorArray.forEach(indicator => {
        let option = document.createElement("option");
        option.value = indicator;
        option.textContent = indicator;
        indicatorDropdown.appendChild(option);
    });

    // Automatically select the first available values
    yearDropdown.value = yearArray[yearArray.length - 1];
    if (indicatorArray.length) indicatorDropdown.value = indicatorArray[0];

    // Trigger initial filter with default selections
    updateMap();
}

function updateMap() {
    const year = document.getElementById("yearDropdown").value;
    const indicator = document.getElementById("indicatorDropdown").value;
    const extractedData = extractByYearAndIndicator(year, indicator);
    console.log(extractedData);

    // Signal that the new data is ready
    document.dispatchEvent(new CustomEvent("dataReady", { detail: extractedData }));
}

let myData = {};
// Fetch the CSV and use it
fetch('./output_folder/mip_sb_data.csv')
    .then(response => response.text())
    .then(csvText => {
        toTable(csvText);

        const rows = document.querySelectorAll("#table tr");

        // Define headers here (from the table DOM, not undefined)
        const headers = Array.from(rows[0].querySelectorAll("th")).map(th => th.textContent.trim());
        // Call dropdown population with correct headers
        populateDropdowns(rows, headers);

        // Get data
        myData = extractByYearAndIndicator("2024", "Current account");
        // Signal that the data is ready
        document.dispatchEvent(new CustomEvent("dataReady", {detail: myData}));
    })
    .catch(error => console.error("Failed to load CSV:", error));

// Listen for dropdown changes
document.getElementById("yearDropdown").addEventListener("change", updateMap);
document.getElementById("indicatorDropdown").addEventListener("change", updateMap);