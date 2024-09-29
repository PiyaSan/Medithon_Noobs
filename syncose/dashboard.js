// Retrieve data from localStorage
const data = JSON.parse(localStorage.getItem('insulinData')) || [];

if (data.length === 0) {
    document.querySelector('.dashboard').innerHTML = '<p>No data available. Please submit your insulin data first.</p><button onclick="window.location.href=\'index.html\'">Back to Form</button>';
} else {
    // Prepare data for charts
    const timestamps = data.map(entry => new Date(entry.timestamp).toLocaleString());
    const timeIntervals = data.map(entry => entry.timeInterval);
    const dosages = data.map(entry => entry.dosage);
    const glucoseLevels = data.map(entry => entry.glucose);

    // Display warnings if any
    let warnings = '';

    data.forEach(entry => {
        if (entry.timeInterval < 4 || entry.timeInterval > 12 || entry.dosage < 2 || entry.dosage > 60 || entry.glucose < 70 || entry.glucose > 250) {
            warnings += `⚠️ Entry on ${new Date(entry.timestamp).toLocaleString()} has parameters out of optimal range.<br>`;
        }
    });

    document.getElementById('warnings').innerHTML = warnings;

    // Chart for Insulin Dosage Over Time
    const ctx1 = document.getElementById('insulinChart').getContext('2d');
    const insulinChart = new Chart(ctx1, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Insulin Dosage (Units)',
                data: dosages,
                backgroundColor: 'rgba(9, 132, 227, 0.2)',
                borderColor: 'rgba(9, 132, 227, 1)',
                borderWidth: 2,
                fill: true
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Time'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Dosage (Units)'
                    },
                    min: 0,
                    max: 100
                }
            }
        }
    });

    // Chart for Blood Glucose Levels Over Time
    const ctx2 = document.getElementById('glucoseChart').getContext('2d');
    const glucoseChart = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Blood Glucose Level (mg/dL)',
                data: glucoseLevels,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255,99,132,1)',
                borderWidth: 2,
                fill: true
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Time'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Glucose Level (mg/dL)'
                    },
                    min: 40,
                    max: 400
                }
            }
        }
    });
}
