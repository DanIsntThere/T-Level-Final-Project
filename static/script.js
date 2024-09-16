ogname = document.title /* Saves original page title */
        document.addEventListener("visibilitychange", function() {
        if (document.visibilityState === 'hidden') {/* If the user switches webpage */
            document.title = "Come back, we miss you";/* The title name will change */
        } else {
            document.title = ogname;/* When they come back it will change back */
        }
});

/*    const navEl = document.querySelector('nav')
  const hamburgerEl = document.querySelector('.hamburger')
  
  hamburgerEl.addEventListener('click',() =>{
    navE1.classList.toggle("nav--open");
    hamburgerEl.classList.toggle("hamburger--open")/* Toggles the menu for smaller dislpays */
 /* }); 
  navEl.addEventListener('click',() =>{
    avEl.classList.remove("nav--open");
    hamburgerEl.classList.remove("hamburger--open")
  }); */
 

  $(document).ready(function() {
    function updateTotalPriceZoo() {
        var adultPrice = parseInt($("#adult_price").text());
        var childPrice = parseInt($("#child_price").text());
        var seniorPrice = parseInt($("#senior_price").text());/*    Gets the values from the html page */
        var numAdult = parseInt($("#num_adult_tickets").val());
        var numChild = parseInt($("#num_child_tickets").val());
        var numSenior = parseInt($("#num_senior_tickets").val());
        var totalPrice = (adultPrice * numAdult) + (childPrice * numChild) + (seniorPrice * numSenior);/* Calculates total */
        $("#total_price").text(totalPrice);/* Outputs total */
        document.getElementById("hidden_Price").value = totalPrice;
    }   

    $(".increment").click(function() {
        var inputField = $(this).prev();
        var currentValue = parseInt(inputField.val());
        inputField.val(currentValue + 1);/* Once the user clicks the + 1 will be added to the current value */
        updateTotalPriceZoo();
    });

    $(".decrement").click(function() {
        var inputField = $(this).next();
        var currentValue = parseInt(inputField.val());
        if (currentValue > 0) {
            inputField.val(currentValue - 1);/*  Once the user clicks the - 1 will be subracted to the current value */
            updateTotalPriceZoo();
        }
    });

    updateTotalPriceZoo();/* Runs the update price at the start */
    function updateTotalPriceHotel(){
        var room = document.getElementById("roomSelect");
        var roomPrice = room.value; /* Gets vaules from form */
        var days = parseInt($("#days").val());
        var totalPrice = (roomPrice * days)/* Calc total price */
        $("#total_price").text(totalPrice);/* Displays total */
        document.getElementById("hidden_Price").value = totalPrice;
    }
    $('#roomSelect').change(function(){
        updateTotalPriceHotel()/* Runs when the select is changed */
    });
    $('#days').change(function(){
        var days = parseInt($("#days").val());
        if ( days> 14) {
            document.getElementById("days").value = 14;
        }
        updateTotalPriceHotel()/* Runs when days is changed */
    });
    updateTotalPriceHotel();
});