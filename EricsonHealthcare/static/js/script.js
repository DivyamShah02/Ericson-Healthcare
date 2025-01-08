function setFormValues(data) {
    // Loop through each key-value pair in the dictionary (data)
    for (const key in data) {
        if (data.hasOwnProperty(key)) {
            // Find the input element(s) where name attribute matches the key
            const input = document.querySelector(`[name="${key}"]`);
            const inputs = document.querySelectorAll(`[name="${key}"]`);

            if (input) {
                if (input.type === 'radio') {
                    // If the input is a radio button group, loop through all radio buttons
                    inputs.forEach(radio => {
                        // Check for true/false values and map them to 'Yes'/'No'
                        if ((data[key] === true || data[key] === "true") && radio.value.toLowerCase() === 'yes') {
                            radio.checked = true;  // Select the "Yes" radio button
                        } else if ((data[key] === false || data[key] === "false") && radio.value.toLowerCase() === 'no') {
                            radio.checked = true;  // Select the "No" radio button
                        } else if (radio.value === data[key]) {
                            // For other radio buttons, match by value
                            radio.checked = true;
                        }
                    });
                } else if (input.type === 'checkbox') {
                    // Handle checkboxes
                    if (Array.isArray(data[key])) {
                        // If the data is an array, check each checkbox that matches
                        inputs.forEach(checkbox => {
                            checkbox.checked = data[key].includes(checkbox.value);
                        });
                    } else {
                        // If it's a single value, just check/uncheck the box
                        input.checked = data[key] === true || data[key] === "true";
                    }
                } else if (input.type === 'file') {
                    const file_input = document.querySelector(`[id="${key}"]`);
                    if (file_input) {
                        if (file_input.tagName === 'A' && data[key] !== null) {
                            let file_input_obj = document.getElementById(key)
                            file_input_obj.style.display = 'block';
                            file_input_obj.href = data[key]
                            file_input_obj.innerText = String(data[key]).split('/').pop();
                        } else {
                            let file_input_obj = document.getElementById(key)
                            file_input_obj.style.display = 'block';
                            file_input_obj.src = data[key]
                        }
                    }
                } else {
                    input.value = data[key];
                }
            }
        }
    }

}

function addSpaces(input) {
    // Check if the input is a string
    if (typeof input !== 'string') {
        console.error('Input must be a string');
        return input; // Return the original string if input is not a string
    }

    // Check if the string is empty
    if (input.trim() === '') {
        console.error('Input string cannot be empty');
        return input; // Return the original string if it's empty
    }

    try {
        // Add space before each capital letter
        return input.replace(/([A-Z])/g, ' $1').trim();
    } catch (error) {
        // Log any unexpected error and return the original string
        console.error('An error occurred while processing the input:', error);
        return input;
    }
}

function showModal(title, content, callback) {
    // Create modal HTML structure
    const modalHtml = `
      <div class="modal fade" id="dynamicConfirmationModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">${title}</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              ${content}
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
              <button type="button" class="btn btn-primary eh-btn-blue-primary-no-hover" id="dynamicConfirmModalButton">Continue</button>
            </div>
          </div>
        </div>
      </div>`;

    // Append the modal to the body
    document.body.insertAdjacentHTML('beforeend', modalHtml);

    // Show the modal
    const modalElement = document.getElementById('dynamicConfirmationModal');
    const bootstrapModal = new bootstrap.Modal(modalElement);
    bootstrapModal.show();

    // Attach event listener to the submit button
    document.getElementById('dynamicConfirmModalButton').addEventListener('click', () => {
        callback(); // Call the provided callback function
        bootstrapModal.hide(); // Hide the modal
        modalElement.remove(); // Remove the modal from the DOM
    });

    // Clean up modal after hiding
    modalElement.addEventListener('hidden.bs.modal', () => {
        modalElement.remove();
    });
}

function displayDocument(url) {
    console.log(url);
    // const domain = window.location.origin;
    const domain = 'https://ericsontpa.pythonanywhere.com';
    const fullUrl = `${domain}${url}`;
    console.log(fullUrl);
    const viewer = document.getElementById('document-viewer');
    viewer.innerHTML = ''; // Clear previous content

    // Get the file extension
    const extension = url.split('.').pop().toLowerCase();

    // Create the appropriate element based on the file type
    if (['jpg', 'jpeg', 'png', 'gif', 'webp'].includes(extension)) {
        // Image
        const img = document.createElement('img');
        img.src = url;
        img.alt = "Image document";
        img.className = 'img-fluid';
        viewer.appendChild(img);
    }
    else if (extension === 'pdf') {
        // PDF
        console.log(url);
        const iframe = document.createElement('iframe');
        iframe.src = fullUrl;
        iframe.allow = "fullscreen";
        iframe.width = "100%";
        iframe.height = "500px";
        viewer.appendChild(iframe);

    }
    else if (['mp4', 'webm', 'ogg'].includes(extension)) {
        // Video
        const video = document.createElement('video');
        video.src = url;
        video.controls = true;
        video.style.width = "100%";
        video.style.maxHeight = '500px';
        viewer.appendChild(video);
    }
    else if (['mp3', 'wav', 'ogg'].includes(extension)) {
        // Audio
        const audio = document.createElement('audio');
        audio.src = url;
        audio.controls = true;
        audio.style.width = "100%";
        audio.style.maxHeight = '500px';
        viewer.appendChild(audio);
    }
    else {
        // Unsupported file type
        viewer.innerHTML = `<p>Unsupported document type: ${extension}</p>`;
    }
}

function displayFinalReportDocument(url) {
    console.log(url);
    const viewer = document.getElementById('final-report-document-viewer');
    viewer.innerHTML = ''; // Clear previous content
    const domain = window.location.origin;
    // const domain = 'https://ericsontpa.pythonanywhere.com';
    const fullUrl = `${domain}${url}`;
    console.log(fullUrl);
    // PDF
    console.log(url);
    const iframe = document.createElement('iframe');
    iframe.src = fullUrl;
    iframe.allow = "fullscreen";
    iframe.width = "100%";
    iframe.height = "500px";
    viewer.appendChild(iframe);


}

