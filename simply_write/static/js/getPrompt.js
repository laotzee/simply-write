const button = document.getElementById('fetchButton');
const textElement = document.getElementById('outputText');

button.addEventListener('click', async () => {
    try {
        // Make the API request
        const response = await fetch('http://127.0.0.1:8000/api/prompt');

        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Get the text from the response
        const data = await response.json();

        // Update the paragraph content
        textElement.textContent = data.body;
    } catch (error) {
        // Handle any errors
        console.error('Error fetching data:', error);
        textElement.textContent = 'Error loading content';
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const notebookButton = document.getElementById('notebookButton');

    if (notebookButton) {
        notebookButton.addEventListener('click', function() {
            try {
                // Get text content
                const pTagElement = document.getElementById('outputText');
                if (!pTagElement) {
                    console.error('Element with id "outputText" not found');
                    return;
                }

                const pTagText = pTagElement.textContent || pTagElement.innerText;

                // Save to browser session storage
                sessionStorage.setItem('prompt_data', pTagText);

                // Redirect to writing page
                window.location.href = 'http://127.0.0.1:8000/writing/';

            } catch (error) {
                console.error('Error in button click:', error);
                // Fallback redirect
                window.location.href = 'http://127.0.0.1:8000/writing/';
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
// Retrieve data from session storage
const promptData = sessionStorage.getItem('prompt_data');

if (promptData) {
    // Populate your textarea or content area
    document.getElementById('outputText').innerHTML = promptData;
    // Clear the data after use (optional)
    sessionStorage.removeItem('prompt_data');
    }
});
