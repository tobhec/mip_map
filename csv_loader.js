function toTable(text){
    let table = document.getElementById("table");
    
    if(!text || !table) {
        return;
    }

    //while(table.lastElementChild){
    //    table.removeChild(table.lastElementChild);
    //}

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

function updateMap() {
    // Extract chosen year and indicator from the dropdown
    const year = document.getElementById("yearDropdown").value;
    const indicator = document.getElementById("indicatorDropdown").value;

    // Extract data from the table
    const extractedData = extractByYearAndIndicator(year, indicator);
    console.log(extractedData);

    // Trigger the data update
    document.dispatchEvent(new CustomEvent("dataReady", { detail: extractedData }));
}

function populateDropdowns(rows, headers, default_year, default_indicator) {
    const yearDropdown = document.getElementById("yearDropdown");
    const indicatorDropdown = document.getElementById("indicatorDropdown");

    const yearSet = new Set();
    const indicatorSet = new Set();

    for (let i = 1; i < rows.length; i++) {
        // Go through the rows and extract the years and indicators
        const cells = rows[i].querySelectorAll("td");
        const year = cells[headers.indexOf("Year")]?.textContent.trim();
        const indicator = cells[headers.indexOf("Indicator")]?.textContent.trim();

        // Add values to dropdown arrays
        if (year) yearSet.add(year);
        if (indicator) indicatorSet.add(indicator);
    }

    // Fill dropdowns with options
    yearSet.forEach(year => {
        let option = document.createElement("option");
        option.value = year;
        option.textContent = year;
        yearDropdown.appendChild(option);
    });
    indicatorSet.forEach(indicator => {
        let option = document.createElement("option");
        option.value = indicator;
        option.textContent = indicator;
        indicatorDropdown.appendChild(option);
    });

    // Set default values for the dropdown
    yearDropdown.value = default_year;
    indicatorDropdown.value = default_indicator;
}

function initiate_map(default_year, default_indicator) {
    // Fetch the CSV and use it
    fetch('./output_folder/mip_sb_data.csv')
        .then(response => response.text())
        .then(csvText => {
            // Convert the CSV to a table
            toTable(csvText);

            // Populate the drop-downs
            const rows = document.querySelectorAll("#table tr");
            const headers = Array.from(rows[0].querySelectorAll("th")).map(th => th.textContent.trim());
            populateDropdowns(rows, headers, default_year, default_indicator);

            // Trigger the initial filter with default selections
            let myData = extractByYearAndIndicator(default_year, default_indicator);
            document.dispatchEvent(new CustomEvent("dataReady", {detail: myData})); ///////////////// Denna ska skickas när allt är laddaat
        })
        .catch(error => console.error("Failed to load CSV:", error));
}

// Load the CSV and initate the map
initiate_map("2024", "Current account");

// Listen for dropdown changes
document.getElementById("yearDropdown").addEventListener("change", updateMap);
document.getElementById("indicatorDropdown").addEventListener("change", updateMap);