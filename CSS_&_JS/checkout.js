let product_quantity = document.querySelectorAll('#product_quantity')
    let product_price = document.querySelectorAll('#product_price');

    let total_price = document.getElementById('total_price');
    let total_cost = document.getElementById('total_cost');
    let total = 0;

    for(let i = 0; i < product_quantity.length; i++){
        let quantity = product_quantity[i].value;
        total += parseInt(quantity) * parseInt(product_price[i].textContent.slice(1));
    }
    total_price.textContent = `$ ${total + 10}`;
    total_cost.value = total;
    // section
    function CheckValid(){
        let cardnumber = document.getElementById('cardnumber')
        let cardexpiration = document.getElementById('cardexpiration')
        let cardcvc = document.getElementById('cardcvc')
        if(cardnumber.value.length != 16 || cardexpiration.value.length!=7 || cardcvc.value.length != 3){
            event.preventDefault();
            alert("Please fill in all required fields.");
        }
    }
    // section
    let cardnumber = document.getElementById('cardnumber');
    let label_cardnumber = document.getElementById('label-cardnumber');
    cardnumber.onchange = function () {
            let num = cardnumber.value;
            let code = "";
            let count = 0;
            for (let i = 0; i < num.length; i++) {
                code += num[i];
                count++;
                if (count === 4) {
                    code += ' - '
                    count = 0;
                }
            }
            label_cardnumber.textContent = code.slice(0, code.length - 2);
        };
    let expiration_input = document.getElementById('cardexpiration');
    let expiration = document.getElementById('label-cardexpiration'); // is going to change
    expiration_input.onchange = () => {
        date = expiration_input.value;
        expiration.textContent = date;
    }
    let cvc_input = document.getElementById('cardcvc');
    let cvc_span = document.getElementById('cvc_span');
    cvc_input.onchange = () =>{
        cvc_code = cvc_input.value;
        cvc_span.textContent = cvc_code;
    }
    
    $(function () {
        $('#cardnumber').payment('formatCardNumber');
        $('#cardexpiration').payment('formatCardExpiry');
        $('#cardcvc').payment('formatCardCVC');

        $('#cardnumber').keyup(function (event) {
            $('#label-cardnumber').empty().append($(this).val());
        });

        $('#cardexpiration').keyup(function (event) {
            var data = $(this).val() + '<span>' + $('#cardcvc').val() + '</span>';
            $('#label-cardexpiration').empty().append(data);
        });

        $('#cardcvc').keyup(function (event) {
            var data = $('#cardexpiration').val() + '<span>' + $(this).val() + '</span>';
            $('#label-cardexpiration').empty().append(data);
        });

        $('.button-cta').on('click', function () {
            var proceed = true;
            $(".field input").each(function () {
                $(this).parent().find('path').each(function () {
                    $(this).attr('fill', '#dddfe6');
                });

                if (!$.trim($(this).val())) {
                    $(this).parent().find('path').each(function () {
                        $(this).attr('fill', '#f1404b');
                        proceed = false;
                    });

                    if (!proceed) {
                        $(this).parent().find('svg').animate({ opacity: '0.1' }, "slow");
                        $(this).parent().find('svg').animate({ opacity: '1' }, "slow");
                        $(this).parent().find('svg').animate({ opacity: '0.1' }, "slow");
                        $(this).parent().find('svg').animate({ opacity: '1' }, "slow");
                    }
                }
            });

            if (proceed)
            {
                $('.field').find('path').each(function () {
                    $(this).attr('fill', '#3ac569');
                });
                $('.payment').fadeToggle('slow', function () {
                    $('.paid').fadeToggle('slow', 'linear');
                });
            }
        });
    });