
let currentSortDirection = 'desc';

function fetchData() {
    let query = $('#search-input').val();
    let sortOption = $('#sort-option').val();
    let genre = $('#genre-filter').val();

    $.ajax({
        url: '/search/',
        data: {
            'q': query,
            'sort': sortOption,
            'direction': currentSortDirection,
            'genre': genre
        },
        dataType: 'json',
        success: function (data) {
            let html = '';
            for (let novel of data) {
                html += `
                    <div class="flex bg-white p-8 gap-4 rounded-2xl shadow-md">
                        <img src="${novel.img_src}" alt="${novel.title}" width="128px" class="rounded-xl">
                        <div class="flex flex-col w-full justify-between">
                            <div>
                                <h3 class="font-raleway font-[700] text-2xl">${novel.title}</h3>
                                <p class="font-montserrat">${novel.author}</p>
                            </div>
                            <div class="">
                                <p class="font-montserrat">Kamu telah membaca 0/${novel.chapters} chapter</p>
                                <div class="bg-gray-300 w-full h-2 rounded-lg shadow-inner">
                                    <div class="bg-blue-500 h-4 rounded-lg transition-all duration-500" style="width: 0%"></div>
                                </div>
                                <p class="font-raleway text-[#101010] opacity-80">Terakhir membaca 28/10/2023</p>
                            </div>
                            <button class="font-raleway px-4 py-2 border-[#115BFB] border-[1px] rounded-xl self-start">Lanjut membaca</button>
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
    $('#genre-filter').on('change', fetchData)
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