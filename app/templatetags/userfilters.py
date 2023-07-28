from django import template

register=template.Library()



@register.filter('swapping') #Swapping is the filter name for swap function
def swap(data):
    return data.swapcase()


@register.filter()
def remove(data,arg):  #It considers function name as Filter name
    return data.replace(arg,'')

    


@register.filter()
def counting(data,sub):
    c=0
    for i in range(len(data)):
        if data[i:i+len(sub):]==sub:
            c+=1
            
    return c

#register.filter('swap',swap)
#register.filter('remove',remove)