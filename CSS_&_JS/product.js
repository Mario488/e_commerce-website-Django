let star1 = document.querySelector('.one-star span');
        let star2 = document.querySelector('.two-stars span');
        let star3 = document.querySelector('.three-stars span');
        let star4 = document.querySelector('.four-stars span');
        let star5 = document.querySelector('.five-stars span');

        let stars_arr = [star1, star2, star3, star4, star5];

        let stars_review = document.querySelectorAll('.starEmoji');
        for(let i = 0; i < stars_review.length; i++){
            let newContent = "";
            for(let j = 0; j < parseInt(stars_review[i].textContent); j++){
                newContent += '\u2B50'; // a star
            }
            stars_review[i].textContent = newContent;
            switch(stars_review[i].textContent.length){

                case 1:
                    star1.textContent += 1;
                    break;
                case 2:
                    star2.textContent += 1;
                    break;
                case 3:
                    star3.textContent += 1;
                    break;
                case 4:
                    star4.textContent += 1;
                    break;
                case 5:
                    star5.textContent += 1;
                    break;
            }

        }

        // section
        let reviews_count = document.querySelectorAll('.review-comment').length;

        let review_count = document.querySelector('.reviews');

        review_count.textContent = reviews_count + ' reviews'; 

        let review_message = document.querySelector('#user-reviews');

        if (reviews_count == 0) {
            review_message.textContent = 'This product currently has no reviews. Be the first to review it!😃';
        }

        let rating = document.querySelector('.rating');
        let avg = 0;
        let arr_length = stars_arr.length;
        
        for(let i = 0; i < arr_length; i++){
            if(stars_arr[i].textContent != ''){
                avg += parseInt(stars_arr[i].textContent * (i + 1)) / reviews_count;
            }
        }
        let avg_stars = document.querySelector('.stars');
        for(let i = 0; i < Math.round(avg); i++){
            avg_stars.textContent += '⭐';
        }

        rating.textContent = `${avg}`;


        // section
        let star_1 = document.getElementById('1-star');
        let star_2 = document.getElementById('2-star');
        let star_3 = document.getElementById('3-star');
        let star_4 = document.getElementById('4-star');
        let star_5 = document.getElementById('5-star');

        let review_desc = document.getElementById('review_desc');

        let star_arr = [star_1, star_2, star_3, star_4, star_5];

        let submit_review = document.querySelector('.submit-review');

        function Rate(num) {
            submit_review.style.display = 'block';
            let review_div = document.createElement('div')
            review_div.classList.add('stars-review');
            for (let i = 0; i < num; i++) {
                review_div.textContent += '⭐';
            }
            submit_review.innerHTML = `
            <form method='POST' action="{% url 'review' %}">
                {% csrf_token %}
                <div class="review-section">
                    <div class="review-header">
                        {% for prod in context.product%}
                        <span><img src="static/{{prod.Series}}.jpg" width="200" height="auto"><br>Review for {{prod.Series}}</span>
                        <input type="hidden" name="product_Name" value="{{prod.Series}}">
                        <input type="hidden" name="stars" value="${num}">
                        {% endfor %}
                        <span class="close" onclick="CloseRate()">❌</span>
                </div>
                <hr>
                <div class="stars-review"></div>
                <div class="review-form">
                    <div class="review-title">
                        <label for="review-title">Title of the review:</label>
                        <input type="text" id="review-title" name="review-title" readonly>
                    </div>
                    <div class="review-content">
                        <label for="review">Review:</label>
                        <textarea id="review" name="review" placeholder="Write your review here" rows="6"></textarea>
                    </div>
                    <button class="add-review-btn">Add Review</button>
                </div>
            </div>
        </form>
        `;
            let review_title = document.getElementById('review-title')
            review_title.value = Message(num);
            submit_review.insertBefore(review_div, submit_review.children[2]);

        }

        function CloseRate() {
            submit_review.style.display = 'none';
            review_desc.textContent = 'Rate the product';
            for (let i = 0; i < star_arr.length; i++) {
                star_arr[i].style.color = 'lightgray';
                star_arr[i].style.transform = 'none';
            }
        }
        function Message(num){
            switch (num) {
                case 1:
                    return 'It is not recommended'
                case 2:
                    return 'Weak';
                case 3:
                    return 'Average';
                case 4:
                    return 'Good';
                case 5:
                    return 'Excellent';
            }
        }
        function starHover(num) {
            review_desc.textContent = Message(num);
            for (let i = 0; i < num; i++) {
                star_arr[i].style.color = 'gold';
                star_arr[i].style.transform = 'scale(1.15)';
            }

        }

        function starUnHover(num) {
            if (submit_review.style.display == 'block'){
                review_desc.textContent = Message(num);
                for(let i = 0; i < num; i++){
                    star_arr[i].style.color = 'gold';
                    star_arr[i].style.transform = 'scale(1.15)';
                }
            }
            else{
                for (let i = 0; i < num; i++) {
                    star_arr[i].style.color = 'lightgray';
                    star_arr[i].style.transform = 'none';
                }
                review_desc.textContent = 'Rate the product';
            }
        }

    // section

    let quantity = document.querySelector('.quantity');
    let quan_input = document.getElementById('quan_input');
    let max_count = document.getElementById('max_count').value;
    let add = document.getElementById('add');
    let count = 1;
    function Add(span){
        if(count == max_count){
            return;
        }
        quantity.innerHTML = `Quantity: <span id="subtract" onclick="Subtract(this)">-</span>${++count}<span id="add" onclick="Add(this)">+</span>`;
        quan_input.value = count;
    }
    function Subtract(span){
        if(count > 1){
            quantity.innerHTML = `Quantity: <span id="subtract" onclick="Subtract(this)">-</span>${--count}<span id="add" onclick="Add(this)">+</span>`;
            quan_input.value = count;
        }
    }
    //zoom
    current_zoom = 1;
        const img = document.querySelector('.product');
        img.addEventListener('click', (event) => {
            const mouseX = event.offsetX;
            const mouseY = event.offsetY;
            current_zoom += 0.6;
            img.style.transformOrigin = `${mouseX}px ${mouseY}px`;
            img.style.transform = `scale(${current_zoom})`;
        })
        img.addEventListener('contextmenu', () => {
            event.preventDefault();
            if (current_zoom > 1) {
                current_zoom -= 0.6;
                img.style.transform = `scale(${current_zoom})`;
            }
        })

    //This is the hover function    
    function Hover(img) {
        const img_change = document.querySelector('.product');
        const first_image = document.querySelector('.mini_Image1');
        const second_image = document.querySelector('.mini_Image2');
        let content = img.getAttribute('src');
        img_change.style.opacity = 0;
        setTimeout(() => {
            img_change.src = content;
            img_change.style.transformOrigin = 'center';
            img_change.style.transform = 'scale(1)';
            current_zoom = 1;
            img_change.style.opacity = 1;
        }, 300);
        if(!(img_change.src.includes('back'))){
            img.style.outline = '2px solid rgb(100, 100, 226)';
            first_image.style.outline = 'none';
        }
        else{
            img.style.outline = '2px solid rgb(100, 100, 226)';
            second_image.style.outline = 'none';
        }
    }