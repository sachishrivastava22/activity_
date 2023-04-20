'''The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.'''
n =int(input("enter wavelength: "))
if 380<=n<450:
    print("violet")
elif 450<=n<495:
    print("Blue")
elif 495<=n<570:
    print("Green")
elif 570<=n<590:
    print("Yellow")
elif 590<=n<620:
    print("orange")
elif 620<=n<=750:
    print("Red")
else:
    print("invalid")
n=n+1

'''
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more

Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message'''
n=float(input("enter frequency:  "))
a=3e9
b=3e12
c=4.3e14
d=7.5e14
e=3e17
f=3e19
if n>a:
    print("Radio wave")
elif a<=n<b:
    print("Microwave")
elif b<=n<c:
    print("Infrared light")
elif c<=n<d:
    print("visible light")
elif d<=n<e:
    print("Ultraviolet light")
elif e<=n<f:
    print("X rays")
elif n>=f:
    print("Gamma rays")
else:
    print("Invalid")