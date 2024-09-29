// Capture form submission
document.getElementById('insulinForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get values from the form
    const timeInterval = parseFloat(document.getElementById('timeInterval').value);
    const dosage = parseFloat(document.getElementById('dosage').value);
    const glucose = parseFloat(document.getElementById('glucose').value);
    const notificationTime = parseFloat(document.getElementById('notificationTime').value);

    // Save data to localStorage for use in dashboard
    const insulinData = {
        timeInterval,
        dosage,
        glucose,
        notificationTime,
        timestamp: new Date().toISOString()
    };

    // Retrieve existing data or initialize an empty array
    const data = JSON.parse(localStorage.getItem('insulinData')) || [];
    data.push(insulinData);

    // Save updated data
    localStorage.setItem('insulinData', JSON.stringify(data));

    // Provide immediate feedback
    let feedback = '';

    // Time Interval Analysis
    if (timeInterval < 4) {
        feedback += '⚠️ Warning: Time between injections is too short (Potential overdose).<br>';
    } else if (timeInterval > 12) {
        feedback += '⚠️ Warning: Time between injections is too long (Potential underdosage).<br>';
    } else {
        feedback += '✅ Time between injections is within the optimal range.<br>';
    }

    // Dosage Analysis
    if (dosage < 2) {
        feedback += '⚠️ Warning: Dosage is too low (Underdosage).<br>';
    } else if (dosage > 60) {
        feedback += '⚠️ Warning: Dosage is too high (Overdosage).<br>';
    } else {
        feedback += '✅ Dosage is within the safe range.<br>';
    }

    // Glucose Level Analysis
    if (glucose < 70) {
        feedback += '⚠️ Warning: Blood glucose level is too low (Hypoglycemia).<br>';
    } else if (glucose > 250) {
        feedback += '⚠️ Warning: Blood glucose level is too high (Hyperglycemia).<br>';
    } else {
        feedback += '✅ Blood glucose level is within the normal range.<br>';
    }

    // Notification Time Analysis
    if (notificationTime < 10 || notificationTime > 720) {
        feedback += '⚠️ Warning: Reminder notification time should be between 10 minutes and 12 hours.<br>';
    } else {
        feedback += '✅ Reminder notification time is set appropriately.<br>';
    }

    // Display feedback
    document.getElementById('feedback').innerHTML = feedback;

    // Redirect to dashboard after a short delay
    setTimeout(() => {
        window.location.href = 'dashboard.html';
    }, 3000);
});

// Capture form submission
document.getElementById('insulinForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get values from the form
    const timeInterval = parseFloat(document.getElementById('timeInterval').value);
    const dosage = parseFloat(document.getElementById('dosage').value);
    const glucose = parseFloat(document.getElementById('glucose').value);
    const notificationTime = parseFloat(document.getElementById('notificationTime').value);

    // Save data to localStorage for use in dashboard
    const insulinData = {
        timeInterval,
        dosage,
        glucose,
        notificationTime,
        timestamp: new Date().toISOString()
    };

    // Retrieve existing data or initialize an empty array
    const data = JSON.parse(localStorage.getItem('insulinData')) || [];
    data.push(insulinData);

    // Save updated data
    localStorage.setItem('insulinData', JSON.stringify(data));

    // Provide immediate feedback (same as your previous implementation)
    // ... (feedback code)

    // Redirect to dashboard after a short delay
    setTimeout(() => {
        window.location.href = 'dashboard.html';
    }, 3000);
});