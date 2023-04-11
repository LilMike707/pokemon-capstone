let serverBaseURL = "http://127.0.0.1:5000/";

$(document).ready(function () {
  $(".like-button").on("click", function () {
    let cardId = $(this).parent().attr("id");
    console.log(`Card Id = ${cardId}`);
    $.ajax({
      url: `${serverBaseURL}addlike`,
      method: "POST",
      data: JSON.stringify({
        card_id: cardId,
      }),
      contentType: "application/json",
      success: function (response) {
        console.log(response);
        // use api data here, if needed
      },
    });
  });
});
