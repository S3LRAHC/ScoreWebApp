document.addEventListener('DOMContentLoaded', function() {
    const scoreForm = document.getElementById('scoreForm');
    const submitForm = document.querySelector('.form-popup .form-container');
    const gradeElement = document.getElementById('grade');
    const plateElement = document.getElementById('plate');
    const scoreElement = document.getElementById('score');

    scoreForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);

        fetch('/calculate', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            updateResults(data);
        })
        .catch(error => console.error('Error:', error));
    });

    submitForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        
        // Add all the necessary data from the page
        formData.append('perfect', document.getElementById('perfect').value);
        formData.append('great', document.getElementById('great').value);
        formData.append('good', document.getElementById('good').value);
        formData.append('bad', document.getElementById('bad').value);
        formData.append('miss', document.getElementById('miss').value);
        formData.append('max_combo', document.getElementById('max_combo').value);
        formData.append('grade', gradeElement.textContent);
        formData.append('plate', plateElement.textContent);
        formData.append('score', scoreElement.textContent);

        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message); // Or update the UI in a more user-friendly way
                closeForm(); // Close the form after successful submission
            } else if (data.error) {
                console.error('Error:', data.error);
                alert('An error occurred while submitting the score.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while submitting the score.');
        });
    });

    function updateResults(data) {
        scoreElement.textContent = data.score;
        gradeElement.textContent = data.grade;
        plateElement.textContent = data.plate;

        const gradeColor = getGradeColor(data.grade);
        gradeElement.style.color = gradeColor;
        toggleShadow(gradeElement, gradeColor);

        const plateColor = getPlateColor(data.plate);
        plateElement.style.color = plateColor;
        toggleShadow(plateElement, plateColor);
    }

    function getGradeColor(grade) {
        if (grade.includes('SSS')) return '#40e8ed';
        if (grade.includes('SS') || grade.includes('S')) return '#f1d93b';
        if (grade.includes('AAA')) return '#a29a8e';
        if (grade.includes('AA') || grade.includes('A')) return '#dca773';
        return '#808080'; // dark gray
    }

    function getPlateColor(plate) {
        if (plate === 'PG' || plate === 'UG') return '#40e8ed';
        if (plate === 'EG' || plate === 'SG') return '#f1d93b';
        if (plate === 'MG' || plate === 'TG') return '#a29a8e';
        return '#dca773';
    }

    function toggleShadow(element, color) {
        if (color !== '#000000') {
            element.classList.add('shadow');
        } else {
            element.classList.remove('shadow');
        }
    }
});