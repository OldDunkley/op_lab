// "import"
const fs = require('fs');

// "calc"
function metricsCalculator(scores) {
    let total = 0;
    for (let i = 0; i < scores.length; i++) {
        total += scores[i];
    }
    const avg = total / scores.length;

    let result = "";
    if (avg > 95) {
        result = "Meeting Expectations";
    } else {
        result = "Needs Improvement";
    }

    console.log(`Average: ${avg} - ${result}`);
}

// Open file
const fileContent = fs.readFileSync('SELECT_score_FROM_UpworkGTNP.tasky_quality.csv', 'utf-8');

// 2. Split into rows
const lines = fileContent.trim().split(/\r?\n/);

// 3. Convert into numbers, skip header
const scores = lines.slice(1).map(Number);

// 4. Run calculation
metricsCalculator(scores);