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

let myData = {};
// Fetch the CSV and use it
fetch('mip_sb_data.csv')
    .then(response => response.text())
    .then(csvText => {
        toTable(csvText);
        myData = extractByYearAndIndicator("2020", "Current account");
        console.log("Extracted data:", myData);
        document.dispatchEvent(new CustomEvent("dataReady", { detail: myData }));
    })
    .catch(error => console.error("Failed to load CSV:", error));
