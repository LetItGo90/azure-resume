window.addEventListener("DOMContentLoaded", (event) =>{
    getVisitCount();
})

const functionApi = 'https://getresumecounter-ekbxcyhhd9erhqdm.eastus-01.azurewebsites.net/api/GetResumeCounter1?code=j8laPYSO3pCjbizz9d1nXDxMWHgb3ghGLg2fVxJy702pAzFuV2jQSA%3D%3D'
const localfunctionApi = 'http://localhost:7071/api/GetResumeCounter'; // Placeholder for the actual API URL

const getVisitCount = () => {
    fetch(functionApi)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Website called function API.");
            const count = data.count || 0; // Fallback to 0 if count is undefined
            document.getElementById("counter").innerText = count;
        })
        .catch(error => {
            console.error("Error fetching visit count:", error);
        });
};

// Call the function to update the counter
getVisitCount();
