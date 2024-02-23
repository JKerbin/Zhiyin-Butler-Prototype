$.ajax({
    url: '/control_api',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({content: 'begin_playing'}),
    success: function(response) {
      window.location.href = "/AIUI.html";}
    })