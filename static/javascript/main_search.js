
let currentSortDirection = 'desc';

function fetchData() {
    let query = $('#search-input').val();
    let sortOption = $('#sort-option').val();
    let genre = $('#genre-filter').val();

    $.ajax({
        url: '/mencari/',
        data: {
            'q': query,
            'sort': sortOption,
            'direction': currentSortDirection,
            'genre': genre
        },
        dataType: 'json',
        success: function (data) {
            let html = '';
            for (let book of data) {
                html += `
                <div class="card bg-white p-4 rounded-lg shadow-lg flex flex-col justify-between">
                    <div class="mb-4 relative">
                        <img src="${book.img_src}" alt="Buku" class="rounded-lg w-full h-auto">
                        <div class="absolute top-4 right-4">
                            <button class="bookmark-button">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="#34D399" class="bookmark-icon h-12 w-12">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="8" d="M4 6a2 2 0 012-2h12a2 2 0 012 2v16l-7-3.5L4 22V6z"></path>
                                </svg>
                            </button>
                        </div>
                    </div>
                    <div>
                        <p class="text-lg font-bold mb-1/2">${book.title}</p>
                        <p class="text-black font-normal mb-2">${book.author}</p>
                        <button class="mt-5 w-full bg-white text-black rounded border border-sky-600 py-2">Baca</button>
                    </div>
                </div>
                `;
            }
            $('#search-results-container').html(html);
        }
    });
}

$(document).ready(function () {
    $('#search-input').on('keyup', fetchData);
    $('#sort-option').on('change', fetchData);
    $('#genre-filter').on('change', fetchData);
});

$('#toggleButton').on('click', function () {
    if (currentSortDirection === 'desc') {
        currentSortDirection = 'asc';
        $('#downArrow').addClass('hidden');
        $('#upArrow').removeClass('hidden');
    } else {
        currentSortDirection = 'desc';
        $('#upArrow').addClass('hidden');
        $('#downArrow').removeClass('hidden');
    }
    fetchData();
});