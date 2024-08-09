document.addEventListener('DOMContentLoaded', function() {
    const scoreForm = document.getElementById('scoreForm');
    const gradeElement = document.getElementById('grade');
    const plateElement = document.getElementById('plate');
    const scoreElement = document.getElementById('score');

    scoreForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);

        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            updateResults(data);
        })
        .catch(error => console.error('Error:', error));
    });

    function updateResults(data) {
        scoreElement.textContent = data.score;

        const gradeColor = getGradeColor(data.grade);
        gradeElement.textContent = data.grade;
        gradeElement.style.color = gradeColor;
        toggleShadow(gradeElement, gradeColor);

        const plateColor = getPlateColor(data.plate);
        plateElement.textContent = data.plate;
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