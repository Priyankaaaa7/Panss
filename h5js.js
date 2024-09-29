// Function to simulate sending a notification
function sendUrgentCareNotification() {
    // Here you would normally send a request to your backend server
    // to notify the doctor and the hospital.
    
    // For demonstration, we'll just return a promise that resolves after a delay
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Urgent care request has been sent to your doctor and the hospital.");
        }, 1000); // Simulate a 1 second delay
    });
}

// Add event listener to the button
document.getElementById('urgent-care-button').addEventListener('click', async () => {
    const notificationDiv = document.getElementById('notification');
    notificationDiv.style.display = "none"; // Hide previous notification

    // Send notification and wait for the response
    const message = await sendUrgentCareNotification();
    
    // Display the notification message
    notificationDiv.innerText = message;
    notificationDiv.style.display = "block"; // Show notification
});
