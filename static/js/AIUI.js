var toggleBtn = document.getElementById("toggleBtn");
var btnUp = true;

toggleBtn.addEventListener("mousedown", function () {
  if (btnUp) {
    btnUp = false;
    $.ajax({
      url: '/control_api',
      method: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({content: 'begin_recording'})
      });
  } else if (!btnUp) {
    btnUp = true;
  }
});

toggleBtn.addEventListener("mouseup", function () {
  $.ajax({
    url: '/control_api',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({content: 'end_recording'}),
    success: function(response) {
      window.location.href = "/AISpeaking.html";}
    })
});

toggleBtn.addEventListener("change", function () {
  if (!btnUp) {
  } else if (btnUp) {
  }
});
