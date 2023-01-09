function initiate_phase1(){
    var target = document.getElementById('selprofile');
    target = target.innerHTML;
    var name = $('#NAME').val();
    var mob = $('#MOBILENO').val();

    $.ajax({
        url: 'register/new/phase1',
        method: 'GET',
        data: {
            'target': target,
            'name': name,
            'mobile': mob,
        },
        success: function(response){
            alert(response['status']);
        }
    })
}