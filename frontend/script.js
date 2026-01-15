document.addEventListener('DOMContentLoaded', () => {
    const scanForm = document.getElementById('scan-form');
    const scanBtn = document.getElementById('scan-btn');
    const btnText = scanBtn.querySelector('.btn-text');
    const loader = scanBtn.querySelector('.loader');
    const resultContainer = document.getElementById('result-container');
    const scoreCircle = document.getElementById('score-circle');
    const scoreText = document.getElementById('score-text');
    const verdictLabel = document.getElementById('verdict-label');
    const explanationList = document.getElementById('explanation-list');
    const resetBtn = document.getElementById('reset-btn');

    scanForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Prepare data
        const urlsInput = document.getElementById('urls').value;
        const data = {
            sender: document.getElementById('sender').value,
            subject: document.getElementById('subject').value,
            body: document.getElementById('body').value,
            urls: urlsInput ? urlsInput.split(',').map(url => url.trim()) : []
        };

        // Loading state
        setLoading(true);

        try {
            const response = await fetch('/analyze-email', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) throw new Error('Analysis failed');

            const result = await response.json();
            displayResult(result);
        } catch (error) {
            console.error(error);
            alert('Something went wrong. Please check if the backend is running.');
            setLoading(false);
        }
    });

    resetBtn.addEventListener('click', () => {
        resultContainer.classList.add('hidden');
        scanForm.classList.remove('hidden');
        scanForm.reset();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    function setLoading(isLoading) {
        if (isLoading) {
            scanBtn.disabled = true;
            btnText.classList.add('hidden');
            loader.classList.remove('hidden');
        } else {
            scanBtn.disabled = false;
            btnText.classList.remove('hidden');
            loader.classList.add('hidden');
        }
    }

    function displayResult(result) {
        setLoading(false);
        scanForm.classList.add('hidden');
        resultContainer.classList.remove('hidden');

        const score = result.risk_score;
        const verdict = result.verdict;
        const explanations = result.explanations;

        // Update score gauge
        scoreCircle.style.strokeDasharray = `${score}, 100`;
        scoreText.textContent = `${score}%`;

        // Set color based on score/verdict
        let color = '#00ff88'; // Safe
        if (score > 30 && score <= 70) color = '#ffcc00'; // Warning
        if (score > 70) color = '#ff3366'; // Danger

        scoreCircle.style.stroke = color;
        verdictLabel.textContent = verdict;
        verdictLabel.style.background = `${color}22`;
        verdictLabel.style.color = color;

        // Clear and fill explanations
        explanationList.innerHTML = '';
        if (explanations && explanations.length > 0) {
            explanations.forEach(reason => {
                const li = document.createElement('li');
                li.textContent = reason;
                explanationList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = "No significant threats detected.";
            explanationList.appendChild(li);
        }

        window.scrollTo({ top: resultContainer.offsetTop - 50, behavior: 'smooth' });
    }
});
