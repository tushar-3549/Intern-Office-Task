document.addEventListener('DOMContentLoaded', function () {
    const inputField = document.getElementById('addr');
    const autocompleteDiv = document.getElementById('autocomplete');
    const countrySelect = document.getElementById('country');

    inputField.addEventListener('input', function() {
        const query = inputField.value.trim();
        if (query.length > 0) {
            fetchSuggestions(query); 
        } else {
            autocompleteDiv.innerHTML = '';  
        }
    });
    function fetchSuggestions(query) {
        const country = countrySelect.value;  
        const apiUrl = `https://geo.bmapsbd.com/bk/v2/autocomplete?text=${encodeURIComponent(query)}&country=${country}`;
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const suggestions = data.places;
                displaySuggestions(suggestions, query); 
            })
            .catch(error => {
                console.error('Error: ', error);
            });
    }
    function displaySuggestions(suggestions, query) {
        autocompleteDiv.innerHTML = '';  
        const filteredSuggestions = suggestions.filter(place => {
            const nameMatch = place.name.toLowerCase().includes(query.toLowerCase());
            const addressMatch = place.address.toLowerCase().includes(query.toLowerCase());
            return nameMatch || addressMatch;
        });
        if (filteredSuggestions.length > 0) {
            filteredSuggestions.forEach(place => {
                const suggestionDiv = document.createElement('div');
                suggestionDiv.classList.add('suggestion');
                suggestionDiv.innerHTML = `${place.name} , ${place.address}`;
                suggestionDiv.addEventListener('click', () => {
                    inputField.value = place.name;  
                    autocompleteDiv.innerHTML = '';  
                });
                autocompleteDiv.appendChild(suggestionDiv);
            });
        } else {
            autocompleteDiv.innerHTML = '<p>No address found</p>';
        }
    }
});








                            // Only work for text perameter

// document.addEventListener('DOMContentLoaded', function () {
//     const inputField = document.getElementById('addr');
//     const autocompleteDiv = document.getElementById('autocomplete');
    
//     inputField.addEventListener('input', function() {
//         const query = inputField.value.trim();
//         if (query.length > 0) {
//             fetchSuggestions(query); 
//         } else {
//             autocompleteDiv.innerHTML = '';  
//         }
//     });
//     function fetchSuggestions(query) {
//         const apiUrl = `https://geo.bmapsbd.com/bk/v2/autocomplete?text=${encodeURIComponent(query)}&country=Pakistan`;
//         fetch(apiUrl)
//             .then(response => response.json())
//             .then(data => {
//                 const suggestions = data.places;
//                 displaySuggestions(suggestions, query); 
//             })
//             .catch(error => {
//                 console.error('Error: ', error);
//             });
//     }
//     function displaySuggestions(suggestions, query) {
//         autocompleteDiv.innerHTML = '';  
//         const filteredSuggestions = suggestions.filter(place => {
//             const nameMatch = place.name.toLowerCase().includes(query.toLowerCase());
//             const addressMatch = place.address.toLowerCase().includes(query.toLowerCase());
//             return nameMatch || addressMatch;
//         });
//         if (filteredSuggestions.length > 0) {
//             filteredSuggestions.forEach(place => {
//                 const suggestionDiv = document.createElement('div');
//                 suggestionDiv.classList.add('suggestion');
//                 suggestionDiv.innerHTML = `${place.name} , ${place.address}`;
//                 // suggestionDiv.innerHTML = `${place.address} - ${place.name}`;
//                 suggestionDiv.addEventListener('click', () => {
//                     inputField.value = place.name;  
//                     autocompleteDiv.innerHTML = '';  
//                 });
//                 autocompleteDiv.appendChild(suggestionDiv);
//             });
//         } else {
//             autocompleteDiv.innerHTML = '<p>No address found</p>';
//         }
//     }
// });






                    // for work only output.jsonl

// document.getElementById('addr').addEventListener('input', function() {
//     const inputValue = this.value.toLowerCase();
//     const suggestions = document.getElementById('autocomplete');
//     suggestions.innerHTML = ''; 

//     if (inputValue.trim() !== '') {
//         fetch('data/output.jsonl')
//             .then(response => response.text())
//             .then(text => {
//                 const lines = text.split('\n').filter(line => line.trim() !== '');

//                 const addressData = lines.map(line => JSON.parse(line));
//                 const filteredData = addressData.filter(item => item.address.toLowerCase().includes(inputValue));

//                 filteredData.forEach(item => {
//                     const suggestionItem = document.createElement('div');
//                     suggestionItem.classList.add('suggestion');

//                     const nameElement = document.createElement('div');
//                     nameElement.textContent = item.name;

//                     const addressElement = document.createElement('div');
//                     addressElement.textContent = `${item.address}`;

//                     suggestionItem.appendChild(addressElement);
//                     suggestionItem.appendChild(nameElement);
                    
//                     suggestionItem.addEventListener('click', function() {
//                         document.getElementById('addr').value = item.address; 
//                         suggestions.innerHTML = ''; 
//                     });
//                     suggestions.appendChild(suggestionItem);
//                 });
//             })
//             .catch(error => console.error('Error :', error));
//     }
// });




