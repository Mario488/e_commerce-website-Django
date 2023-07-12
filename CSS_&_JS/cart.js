function GetData() {
        let product = document.querySelectorAll('#phone_Series');
        let pr_quantity = document.querySelectorAll('#product_Quantity');
        let price = document.querySelectorAll('#price');

        let input_prices = document.getElementById('product_price');
        let input_products = document.getElementById('products');
        let input_quantityes = document.getElementById('quantities');

        let product_string = "";
        let pr_quantity_string = "";
        let prices = "";
        for (let i = 0; i < product.length; i++) {
            if (i == product.length - 1) {
                product_string += product[i].textContent;
                break;
            }
            product_string += product[i].textContent + ",";
        }

        for (let i = 0; i < pr_quantity.length; i++) {
            if (i == pr_quantity.length - 1) {
                pr_quantity_string += pr_quantity[i].textContent;
                break;
            }
            pr_quantity_string += pr_quantity[i].textContent + ",";
        }

        for (let i = 0; i < price.length; i++) {
            let index = price[i].textContent.slice(7).indexOf(" ")
            sliced = price[i].textContent.slice(7);

            if (i == price.length - 1) {
                prices += sliced.slice(0, index);
                break;
            }
            prices += sliced.slice(0, index) + ",";
        }
        input_products.value = product_string;
        input_quantityes.value = pr_quantity_string;
        input_prices.value = prices;
    }



    // get all the quantity elements
    const quantityElements = document.querySelectorAll("#quantity");

    quantityElements.forEach((quantityElement) => {
        const quantity = quantityElement.querySelector(".q");
        let max_count = quantityElement.querySelector('#max_count').value;
        let addButton = quantityElement.querySelector('.add');
        if (quantity.textContent == max_count) {
            addButton.style.backgroundColor = '#7f7f7f';
            addButton.style.color = 'rgb(187, 167, 167)';
        }
    })
    // loop through each element and add event listeners
    quantityElements.forEach((quantityElement) => {
        const subtractButton = quantityElement.querySelector(".subtract");
        const addButton = quantityElement.querySelector(".add");
        const quantityValue = quantityElement.querySelector(".q");

        let max_count = quantityElement.querySelector('#max_count');

        subtractButton.addEventListener("click", () => {
            // get the current quantity value and convert it to a number
            let quantity = quantityValue.textContent;

            // decrease the quantity by 1 if it's greater than 0
            if (quantity > 1) {
                quantity--;
                quantityValue.textContent = quantity;
                addButton.style.backgroundColor = 'black';
                addButton.style.color = '#fff';
            }

            let subtotal = document.getElementById('subtotal');
            let total = document.getElementById('total');

            let price = document.querySelectorAll('#price');
            let q = document.querySelectorAll('.q');

            let subtotal_price = 0;
            let total_price = 0;
            for (let i = 0, j = 0; i < price.length && j < q.length; i++, j++) {
                subtotal_price += parseInt(price[i].textContent.match(/[\d.]+/).join()) * q[i].textContent;
            }
            total_price = subtotal_price + 10;
            subtotal.textContent = `$ ${subtotal_price}`;
            total.textContent = `$ ${total_price}`;
        });

        addButton.addEventListener("click", () => {
            // get the current quantity value and convert it to a number
            let quantity = quantityValue.textContent;
            // increment the quantity by 1
            if (quantity < max_count.value) {
                quantity++;
                quantityValue.textContent = quantity;
                if (quantity == max_count.value) {
                    addButton.style.backgroundColor = '#7f7f7f';
                    addButton.style.color = 'rgb(187, 167, 167)';
                }
                let subtotal = document.getElementById('subtotal');
                let total = document.getElementById('total');

                let price = document.querySelectorAll('#price');
                let q = document.querySelectorAll('.q');

                let subtotal_price = 0;
                let total_price = 0;
                for (let i = 0, j = 0; i < price.length && j < q.length; i++, j++) {
                    subtotal_price += parseInt(price[i].textContent.match(/[\d.]+/).join()) * q[i].textContent;
                }
                total_price = subtotal_price + 10;
                subtotal.textContent = `$ ${subtotal_price}`;
                total.textContent = `$ ${total_price}`;
            }
            else {
                return;
            }
        });
    });
    // for price 
    let subtotal = document.getElementById('subtotal');
    let total = document.getElementById('total');
    var del_cost = document.getElementById('del-cost');

    let price = document.querySelectorAll('#price');
    let q = document.querySelectorAll('.q');


    let subtotal_price = 0;
    let total_price = 0;
    for (let i = 0, j = 0; i < price.length && j < q.length; i++, j++) {
        subtotal_price += parseInt(price[i].textContent.match(/[\d.]+/).join()) * q[i].textContent;
    }
    total_price = subtotal_price + parseInt(del_cost.textContent.substring(0, 2));
    subtotal.textContent = `$ ${subtotal_price}`;
    total.textContent = `$ ${total_price}`;

    // checking cart
    let items = document.querySelectorAll('.cart-item');
    let state = document.getElementById('state');
    if (items.length == 0) {
        state.textContent = 'The shopping cart is empty';
        state.style.textAlign = 'center';
        del_cost.textContent = '$0';
        checkout_btn = document.getElementById('checkout_btn');
        checkout_btn.disabled = true;
        checkout_btn.style.cursor= 'not-allowed';
        total.textContent = '$0';
    }
    else {
        del_cost.textContent = '$ 10';
    }
