$(function () {
    $(".btn-delete").click(function () {
      var id = $(this).attr('data-id');
      if (confirm("Are your sure?")) {
        $.ajaxSetup({
          headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
          }
        });
  
        $.ajax({
          url: url,
          method: 'POST',
          data: { id: id },
          success: function (result) {
            if (result.success) {
              alert(result.message);
              window.location.reload()
            } else {
              alert(result.message);
            }
          }
        });
      }
    });
  });
  