function searchCourse() {
  const searchBar = document.getElementById("searchBar");
  const courseCode = searchBar.value.trim().toLowerCase();

  // Check if the courseCode matches the expected pattern
  const pattern = /^cs\d+$/;
  if (!pattern.test(courseCode)) {
    alert(
      "Invalid input. Please enter a valid course code in the format cs<number>."
    );
    return;
  }
  var returnVal = populateCourseDetails(courseCode);
  console.log(returnVal);
}

function populateCourseDetails(courseCode) {
  const apiUrl = `http://127.0.0.1:5000/api/v1.0/courseDetails?code=${courseCode}`;

  // Fetch data from the API
  fetch(apiUrl)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // Populate the table with the response data
      const tableBody = document.getElementById("courseDetailsBody");
      tableBody.innerHTML = "";
      
      // append the following rows to table body. clear existing
      const order = [
        "title",
        "year",
        "semester",
        "instructor",
        "venue",
        "slot",
        "clashing_courses",
        "difficulty",
        "strength",
      ];

      order.forEach((key) => {
        if (data.hasOwnProperty(key)) {
          const row = tableBody.insertRow("tr");
          const attributeCell = document.createElement("td");
          const valueCell = document.createElement("td");
          row.classList.add("text-center");

          valueCell.textContent = formatValue(data[key]);
          if (key == "code") {
            key = "Course Code";
          }

          if (key == "clashing_courses") {
            key = "Clashing Courses";
            row.classList.add("table-danger");
          }

          if (key == "difficulty") {
            row.classList.add("table-warning");
          }

          if (key == "strength") {
            row.classList.add("table-success");
          }

          attributeCell.innerHTML = formatValue(key);
          attributeCell.classList.add("font-weight-bold");
          row.appendChild(attributeCell);
          row.appendChild(valueCell);
          tableBody.appendChild(row);
        }
      });

      // tableBody.style.display = "block";
      // fetchImages(courseCode);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      tableBody.style.display = "none";
    });
}


function formatValue(value) {
  // Format the value as needed (e.g., capitalize the first letter)
  return String(value).charAt(0).toUpperCase() + String(value).slice(1);
}
async function fetchImages(filename) {
  try {
    const response = await fetch(
      `http://127.0.0.1:5000/api/v1.0/get_images/${filename}`
    );
    const data = await response.json();

    const imageContainer = document.getElementById("imageContainer");
   
      imageContainer.innerHTML = "";
      if(data.image_paths.length != 0){
      imageContainer.innerHTML = "Grading Plots for Previous Years";}
      imageContainer.classList.add("text-center");
      imageContainer.classList.add("h4");

      data.image_paths.forEach((image) => {
        const fig = document.createElement("figure");
        fig.classList.add("mx-auto");

        const img = document.createElement("img");
        img.src = image.path;
        img.alt = `Graph analysis for ${image.year} year`;
        img.height = 400;
        img.width = 600;

        const heading = document.createElement("figcaption");
        heading.classList.add("figure-caption");
        heading.textContent = `Year: ${image.year}`;
        fig.appendChild(img);
        fig.appendChild(heading);

        imageContainer.appendChild(fig);
      });
    
  } catch (error) {
    console.error("Error fetching images:", error);
  }
}
