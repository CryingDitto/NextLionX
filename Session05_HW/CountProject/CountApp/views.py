from django.shortcuts import render

# Create your views here.

#count function
def count(request):    
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    total_byte = countbyte(text)
    no_blank_len = len(text.replace(' ', ''))
    no_blank_byte = countbyte(text.replace(' ', ''))
    word_len = countword(text)
    return render(request, 'result.html', {'input_text': text,
                                           'total_len': total_len,
                                           'no_blank_len': no_blank_len,
                                           'total_byte':total_byte,
                                           'no_blank_byte':no_blank_byte,
                                           'word_len':word_len,} )


def countbyte(text):
    return len(text.encode())

def countword(text):
    return len(text.split(' '))
