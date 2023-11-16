document.addEventListener('DOMContentLoaded', function () {
    // Replace this with your actual API endpoint
    const apiUrl = 'http://127.0.0.1:5000/api/v1.0/courseDetails?code=22';
  
    // Fetch data from the API
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        // Populate the table with the response data
        const tableBody = document.getElementById('courseDetailsBody');
  
        for (const key in data) {
          if (data.hasOwnProperty(key)) {
            const row = document.createElement('tr');
            const attributeCell = document.createElement('td');
            const valueCell = document.createElement('td');
  
            attributeCell.textContent = key;
            valueCell.textContent = data[key];
  
            row.appendChild(attributeCell);
            row.appendChild(valueCell);
            tableBody.appendChild(row);
          }
        }
      })
      .catch(error => console.error('Error fetching data:', error));
  });
  