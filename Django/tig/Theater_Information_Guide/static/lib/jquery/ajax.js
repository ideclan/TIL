$(document).ready(function () {
    $('#sort-select').change(function () {
        var option = $("#sort-select option:selected").val();
        var active = $("ul>li");
        active.removeClass('active');
        $('#page-01').addClass('active');
        $.ajax({
            url: '/change_option/',
            data: {option: option},
            success: function (data) {
                var opt_data = data.theater_data;
                var num = data.theater_data.length;
                $("div").remove("#theater_body");
                for (var i = 0; i < num; i++) {
                    $("#change-option").append(
                        '<div class="col-md-4" id="theater_body">' +
                        '<div class="card-box-a card-shadow">' +
                        '<div class="img-box-a">' +
                        '<img src="' +
                        '/static/'
                        + opt_data[i].image +
                        '" alt="" class="img-a img-fluid">' +
                        '</div>' +
                        '<div class="card-overlay">' +
                        '<div class="card-overlay-a-content">' +
                        '<div class="card-header-a">' +
                        '<h2 class="card-title-a">' +
                        '<a>' + opt_data[i].id + '위' +
                        '<br/>' + opt_data[i].name + '</a>' +
                        '</h2>' +
                        '</div>' +
                        '<div class="card-body-a">' +
                        '<div class="price-box d-flex">' +
                        '<span class="price-a">Price | $ ' + opt_data[i].price + '</span>' +
                        '</div>' +
                        '<a href="/theaters/' +
                        opt_data[i].id +
                        '/" class="link-a">Click here to view' +
                        '<span class="ion-ios-arrow-forward"></span>' +
                        '</a>' +
                        '</div>' +
                        '<div class="card-footer-a">' +
                        '<ul class="card-info d-flex justify-content-around">' +
                        '<li>' +
                        '<h4 class="card-info-title">기간</h4>' +
                        '<span>' + opt_data[i].period + '</span>' +
                        '</li>' +
                        '<li>' +
                        '<h4 class="card-info-title">장소</h4>' +
                        '<span>' + opt_data[i].place + '</span>' +
                        '</li>' +
                        '</ul>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</div>'
                    );
                }
            }
        });
    });
});

$(document).ready(function () {
    $(".page-item").on("click", function () {

        var pre_data = $(".page-item.active ").attr("id");
        var cli_data = $(this).attr("id");

        var option = $("#sort-select option:selected").val();
        var active = $("ul>li");
        active.removeClass('active');

        if (cli_data == "page-previous") {
            if (pre_data == "page-03") {
                var page = "page-02"
            } else {
                var page = "page-01"
            }
        } else if (cli_data == "page-next") {
            if (pre_data == "page-01"
            ) {
                var page = "page-02";
            } else {
                var page = "page-03";
            }
        } else {
            var page = cli_data;
        }
        $("#" + page).addClass('active');


        $.ajax({
            url: '/change_page/',
            data: {
                page: page,
                option: option,
            },
            success: function (data) {
                var opt_data = data.theater_data;
                var num = data.theater_data.length;
                $("div").remove("#theater_body");
                for (var i = 0; i < num; i++) {
                    $("#change-option").append(
                        '<div class="col-md-4" id="theater_body">' +
                        '<div class="card-box-a card-shadow">' +
                        '<div class="img-box-a">' +
                        '<img src="' +
                        '/static/'
                        + opt_data[i].image +
                        '" alt="" class="img-a img-fluid">' +
                        '</div>' +
                        '<div class="card-overlay">' +
                        '<div class="card-overlay-a-content">' +
                        '<div class="card-header-a">' +
                        '<h2 class="card-title-a">' +
                        '<a>' + opt_data[i].id + '위' +
                        '<br/>' + opt_data[i].name + '</a>' +
                        '</h2>' +
                        '</div>' +
                        '<div class="card-body-a">' +
                        '<div class="price-box d-flex">' +
                        '<span class="price-a">Price | $ ' + opt_data[i].price + '</span>' +
                        '</div>' +
                        '<a href="/theaters/' +
                        opt_data[i].id +
                        '/" class="link-a">Click here to view' +
                        '<span class="ion-ios-arrow-forward"></span>' +
                        '</a>' +
                        '</div>' +
                        '<div class="card-footer-a">' +
                        '<ul class="card-info d-flex justify-content-around">' +
                        '<li>' +
                        '<h4 class="card-info-title">기간</h4>' +
                        '<span>' + opt_data[i].period + '</span>' +
                        '</li>' +
                        '<li>' +
                        '<h4 class="card-info-title">장소</h4>' +
                        '<span>' + opt_data[i].place + '</span>' +
                        '</li>' +
                        '</ul>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '</div>'
                    );
                }
            }
        });
    });
});
