
function fetchResults() {
    const query = document.getElementById('search-input').value;
    const resultsContainer = document.getElementById('results-container');

    if (query.length > 0) {
        fetch(`/search_users?query=${query}`)
            .then(response => response.json())
            .then(data => {
                resultsContainer.innerHTML = '';
                if (data.length > 0) {
                    let ul = document.createElement('ul');
                    data.forEach(user => {
                        let li = document.createElement('li');
                        li.textContent = user.username;
                        li.onclick = () => window.location.href = `/profile/${user.username}`;
                        ul.appendChild(li);
                    });
                    resultsContainer.appendChild(ul);
                    resultsContainer.style.display = 'block';
                } else {
                    resultsContainer.innerHTML = '<ul><li>No results found</li></ul>';
                    resultsContainer.style.display = 'block';
                }
            });
    } else {
        resultsContainer.style.display = 'none';  // Hide the results container if the query is empty
    }
}


// Hide the search results when clicking outside the search area
document.addEventListener('click', function (event) {
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('results-container');

    if (!searchInput.contains(event.target) && !resultsContainer.contains(event.target)) {
        resultsContainer.style.display = 'none';
    }
});

