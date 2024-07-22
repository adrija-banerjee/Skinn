const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const capture = document.getElementById('capture');
const result = document.getElementById('result');
const capturedImage = document.getElementById('capturedImage');
const upload = document.getElementById('upload');
const uploadBtn = document.getElementById('upload-btn');

// Access the device camera and stream to video element
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(console.error);

capture.addEventListener('click', () => {
    // Ensure the camera is ready before capturing
    if (video.readyState === video.HAVE_ENOUGH_DATA) {
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const dataUrl = canvas.toDataURL('image/jpeg');
        
        // Display the captured image
        capturedImage.src = dataUrl;

        // Send the captured image to the server for prediction
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: dataUrl })
        })
        .then(response => response.json())
        .then(data => {
            result.textContent = `Predicted Acne Level: ${data.predicted_class}`;
        })
        .catch(console.error);
    }
});

uploadBtn.addEventListener('click', () => {
    const file = upload.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = () => {
            const dataUrl = reader.result;
            capturedImage.src = dataUrl;
            
            // Send the uploaded image to the server for prediction
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image: dataUrl })
            })
            .then(response => response.json())
            .then(data => {
                result.textContent = `Predicted Acne Level: ${data.predicted_class}`;
            })
            .catch(console.error);
        };
        reader.readAsDataURL(file);
    }
});
