from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    
    context = {
    	
    	"my_list": [{
    		"restaurant_name": "foo1",
    		"food_type": "oof1",
    	},
    	
    	{
    		"restaurant_name": "foo2",
    		"food_type": "oof2",
    	},
    	
    	{
    		"restaurant_name": "foo3",
    		"food_type": "oof3",
    	}],
    }

    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {
            "restaurant_name": "foo1",
            "food_type": "foo2",
            "fav_rest": "fav1"
        }
    }
    return render(request, 'detail.html', context)
