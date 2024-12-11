async function callApi(method, url, bodyData = null, csrfToken = '') {
    try {
        // Validate method and URL
        if (typeof method !== 'string' || typeof url !== 'string') {
            throw new Error("Invalid method or URL");
        }

        // Prepare request options
        const options = {
            method: method.toUpperCase(),
            headers: {
                'Content-Type': 'application/json',
                ...(csrfToken && { 'X-CSRFToken': csrfToken }), // Add CSRF token if provided
            },
        };

        // Add bodyData for non-GET requests
        if (method.toUpperCase() !== 'GET' && bodyData) {
            options.body = JSON.stringify(bodyData);
        }

        // Make the fetch request
        const response = await fetch(url, options);

        // Check for HTTP errors
        // if (!response.ok) {
        //     throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
        // }

        // Parse the JSON response
        const data = await response.json();

        // Return success flag and data
        return [true, data];
    } catch (error) {
        // Log and return failure flag with error
        console.error("API Call Error:", error);
        return [false, error.message || "An unknown error occurred"];
    }
}

function toQueryString(params) {
    return Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&');
}


// Example Usage of api caller function
async function exampleApiCallerPOST() {
    const bodyData = {
        email: "divyamshah1234@gmail.com",
        password: "divym",
    };

    const url = "{% url 'login-api-list' %}";
    const [success, result] = await callApi("POST", url, bodyData, "{{csrf_token}}");
    if (success) {
        console.log("Login User Success:", result);
    } else {
        console.error("Login User Failed:", result);
    }
}


async function exampleApiCallerGET() {
    const Params = {
        user_id: "IO7169754192",
    };

    const url = "{% url 'user-list' %}?" + toQueryString(Params); // Construct the full URL with query params
    const [success, result] = await callApi("GET", url);
    if (success) {
        console.log("GET User Success:", result);
    } else {
        console.error("GET User Failed:", result);
    }
}
