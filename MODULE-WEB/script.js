document.addEventListener('DOMContentLoaded', function () {
    const courseCodes=["CS 601", "CS 618", "CS 725" , "CS 742"];

    function handleKeyDown(event){
      if(event.key == "Enter"){
        searchCourse();
      }
    }
    function searchCourse(){
      const searchBar= document.getElementById("searchBar");
      const courseDetailsContainer= document.getElementById("courseDetailsContainer");

      const enteredCode= searchBar.value.toUpperCase();
      if(courseCodes.includes(enteredCode)){
        courseDetailsContainer.style.display="block";
        populateCourseDetails(enteredCode);
      }
      else{
        courseDetailsContainer.style.display="none";
      }
    }

    function populateCourseDetails(courseCde){
      // Replace this with your actual API endpoint
      const apiUrl = 'http://127.0.0.1:5000/api/v1.0/courseDetails?code=${courseCode}';
    
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
    }
  });
  