document.addEventListener("DOMContentLoaded", () => {

    document.addEventListener('click',event => {
        
        if (event.target.id === "add-cart-button")
        {   event.preventDefault();
            const add_cart_button_id = event.target.dataset.pid
            const item_class = event.target.dataset.type
            const item_name = event.target.dataset.item
            const size_chooser = `#${item_class}-size-${add_cart_button_id}`
            var sel = document.querySelector(size_chooser)
            const size = sel.value          
            const quantity_chooser = `#${item_class}-quantity-${add_cart_button_id}`
            const quantity = parseInt(document.querySelector(quantity_chooser).value)
            if (!quantity || size === "none")
            {
                alert("Please Choose size and quantity")
            }
            
            token = document.querySelector('[name=csrfmiddlewaretoken]').value
            
            var request = new XMLHttpRequest()          
            request.open('POST','/addcart')
            request.setRequestHeader('X-CSRFToken', token);
            request.onload = () => {
                const data = JSON.parse(request.responseText)
                if(data.status)
                {
                    alert(`successfully added ${quantity} ${item_name} to Cart`)
                }
                if(!data.status)
                {
                    alert("You Must Login First")
                }
                if(data.status === "server error")
                {
                    alert("Server Error Please Try Again")
                }
            }

            
            var data = new FormData()
            data.append('item_class',item_class)
	    data.append('item_id',add_cart_button_id)
            data.append('item_name',item_name)
            data.append('size',size)
            data.append('quantity',quantity)
            request.send(data)
            document.querySelector(quantity_chooser).value = ""
            document.querySelector(size_chooser).value = "none"
        }
        if(event.target.id === "add-cart-button-2")
        {event.preventDefault();
            const add_cart_button_id = event.target.dataset.pid
            const item_class = event.target.dataset.type
            const item_name = event.target.dataset.item   
            const quantity_chooser = `#${item_class}-quantity-${add_cart_button_id}`
            const quantity = parseInt(document.querySelector(quantity_chooser).value)

            if (!quantity)
            {
                alert("Please Choose Quantity")
            }
            token = document.querySelector('[name=csrfmiddlewaretoken]').value
            var request = new XMLHttpRequest()          
            request.open('POST','/addcart')
            request.setRequestHeader('X-CSRFToken', token);
            request.onload = () => {
                const data = JSON.parse(request.responseText)
                if(data.status)
                {
                    alert(`successfully added ${quantity} ${item_name} to Cart`)
                }
                else
                {
                    alert("You Must Login First")
                }
            }
            var data = new FormData()
            data.append('item_class',item_class)
	    data.append('item_id',add_cart_button_id)
            data.append('item_name',item_name)
            data.append('quantity',quantity)
            request.send(data)
            document.querySelector(quantity_chooser).value = ""
            
        }
    })

})
