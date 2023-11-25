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
  // Replace this with your actual API endpoint
  const apiUrl = `http://127.0.0.1:5000/api/v1.0/courseDetails?code=${courseCode}`;

  // Fetch data from the API
  fetch(apiUrl)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // Populate the table with the response data
      const tableBody = document.getElementById("courseDetailsBody");
      // append the following rows to table body. clear existing
      tableBody.innerHTML = "";
      const order = [
        "code",
        "title",
        "instructor",
        "slot",
        "venue",
        "difficulty",
        "projects",
        "recommended",
        "strength",
      ];

      order.forEach((key) => {
        if (data.hasOwnProperty(key)) {
          const row = document.createElement("tr");
          const attributeCell = document.createElement("td");
          const valueCell = document.createElement("td");

          valueCell.textContent = formatValue(data[key]);
          if (key == "code") {
            key = "Course Code";
          }

          if (key == "projects") {
            key = "Contains Projects";
          }
          attributeCell.textContent = formatKey(key);
          attributeCell.classList.add("font-weight-bold");
          row.appendChild(attributeCell);
          row.appendChild(valueCell);
          tableBody.appendChild(row);
        }
      });

      tableBody.style.display = "block";
      fetchImages(courseCode);
      return true;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      tableBody.style.display = "none";
      return false;
    });
  // return true if data is found
}
function formatKey(key) {
  // Capitalize the first letter of each word
  return key.replace(/(?:^|\s)\S/g, (char) => char.toUpperCase());
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

    data.image_paths.forEach((image) => {
      const img = document.createElement("img");
      img.src = image.path;
      img.alt = `Graph analysis for ${image.year} year`;

      const heading = document.createElement("h6");
      heading.textContent = `Year: ${image.year}`;

      imageContainer.appendChild(heading);
      imageContainer.appendChild(img);
    });
  } catch (error) {
    console.error("Error fetching images:", error);
  }
}
