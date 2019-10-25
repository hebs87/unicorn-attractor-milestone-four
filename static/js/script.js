/*
* Initialize all Materialize elements
*/
function materializeInit() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
}
materializeInit();

/*
* Flash Messages
* Display for 3 seconds
*/
function flashMessage() {
    $("#flash_message").addClass("show");
    setTimeout(function () {
        $("#flash_message").removeClass("show");
    }, 3000);
}
flashMessage();