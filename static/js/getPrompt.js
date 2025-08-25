const button = document.getElementById('fetchButton');
const textElement = document.getElementById('outputText');

document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('fetchButton');

    if (button) {
        button.addEventListener('click', async () => {
            try {
                const apiUrl = button.dataset.apiUrl;
                const response = await fetch(apiUrl);

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                const outputText = document.getElementById('output-text');

                // Force animation restart
                outputText.style.animation = 'none';
                outputText.offsetHeight;
                outputText.style.animation = null;

                outputText.textContent = data.body;

            } catch (error) {
                console.error('Error fetching data:', error);
                const outputText = document.getElementById('output-text');
                outputText.textContent = 'Error loading content';
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const notebookButton = document.getElementById('notebookButton');

    if (notebookButton) {
        notebookButton.addEventListener('click', function() {
            try {
                // Get text content
                const pTagElement = document.getElementById('output-text');
                if (!pTagElement) {
                    console.error('Element with id "outputText" not found');
                    return;
                }

                const pTagText = pTagElement.textContent || pTagElement.innerText;

                // Save to browser session storage
                sessionStorage.setItem('prompt_data', pTagText);


            } catch (error) {
                console.error('Error in button click:', error);
                // Fallback redirect
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
// Retrieve data from session storage
const promptData = sessionStorage.getItem('prompt_data');

if (promptData) {
    // Populate your textarea or content area
    document.getElementById('output-text').innerHTML = promptData;
    // Clear the data after use (optional)
    sessionStorage.removeItem('prompt_data');
    }
});
