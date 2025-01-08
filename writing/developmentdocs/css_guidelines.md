# Development Guidelines for CSS

The aim of this document is to outline the rules and best practices we follow while writing CSS for the development. By reviewing this document, you will gain a clear understanding of the key steps to follow during development.

## 0. Why we prefer rem instead of px ?

- One important guideline is to prefer using **rem** units over **px** when defining sizes in CSS. The primary reason is that **rem** units are relative to the root element's font size, making designs more scalable and responsive.
- This means that by simply adjusting the root font size, you can proportionally scale all **rem**-based elements, which is particularly useful for creating responsive designs.
- Additionally, **rem** enhances accessibility by respecting user preferences for font scaling, ensuring better readability for those who adjust browser font sizes.
  > 1 rem = 16 px

While in some cases we use **px** unit like for box shadows or custom cursors were we want the component to stay of the same size irrespective of the screen size.

## 1. Why we switched from rem to vw?

While testing out our websites we came across an issue that the UI of the websites were working completely fine for the base resolution screens and screens smaller than base resolution but the UI was breaking when we switch to a bigger size screen than the base resolution.

To overcome this we revamped the complete CSS of our websites where we replaced the px values with a suitable vw values and ensuring that it does not changes the original UI of the web-pages.

**Site used to calculate the perfect vw:**
[CSS Unit Converter](https://cssunitconverter.vercel.app/rem-to-vw)

## 2. Responsiveness

We use media queries to handle the responsiveness of the web-pages where we try to get every minute detail for any type of devices.
One important point to keep in mind while writing media queries is that we do not repeat any css styles which will be constant for all the devices like the font-color, background-color, etc.

    body{
        font-size: 16px;
    }

    @media (max-width: 768px){
        body{
    	    font-size: 18px;
        }
    }

> **max-width:** Style will apply for screens smaller that the specified px size.
> **min-width:** Style will apply for screens bigger than the specified px size.
> **[ same goes for height ]**

## 3. Handle CSS not being compatible with safari browsers

Safari sometimes handle CSS differently than other browsers, which leads to compatibility issues. like animations are not working correctly.

### 3.1 Incompatible CSS styles :

safari sometimes handles CSS differently that other browsers, leading to compatibility issues.
**eg :**

    .container{
        appearance: none;
    }

This will now always work for safari to overcome this issue we use a prefix `-webkit-`
**updated code :**

    .container[
        -webkit-appearance: none;
        appearance: none;
    }

### 3.2 Incompatible JS functions :

safari does not support some JS functions which we use to style the components and we need to use another prebuilt function that can carry out same task.
**eg :**

    customContainer.animate(
        left: 20px;
        top: 20px;
    );

here, the `.animate()` function is not supported by safari and hence we used `requestAnimationFrame()` function:

    requestAnimationFrame(() => {
        customContainer.style.left = `20px`;
        customContainer.style.top = `20px`;
    });
