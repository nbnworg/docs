# ReactJS to NextJS Migration Using App Router In Server Side Rendering


## Introduction To NextJS
Next.js is a React framework for building full-stack web applications. You use React Components to build user interfaces, and Next.js for additional features and optimizations. Under the hood, Next.js also abstracts and automatically configures tooling needed for React, like bundling, compiling, and more. This allows you to focus on building your application instead of spending time with configuration.
NextJS provides us various features such as:-

 1. Routing:- File based routing that supports layout, loading state, error state, nested routing
 2. Rendering:- Client side and Server side rendering with client and server components.
 3. Data Fetching:- Using async/await data can be fetched easily or using the fetch API 
 
 
## How to build SSR NextJS Application
To start building the Server Side Rendered NextJS application using app router you first need to structurized you files in proper way, what all routes you have you need to create folder with the name exactly as the route name because NextJS support file based routing

And all this routing files fill be created inside the app directory (i.e when you install the nextjs using `npm create-next-app@latest` Once you execute this command the nextjs will start getting installed and after few seconds you will see some installations specific question where you have to opt for the options accodingly. Below is sample of the same

> What is your project named? my-app
Would you like to use TypeScript? Yes
Would you like to use ESLint? No
Would you like to use Tailwind CSS? No
Would you like your code inside a `src/` directory? Yes
Would you like to use App Router? (recommended) Yes
Would you like to use Turbopack for `next dev`?  No
Would you like to customize the import alias (`@/*` by default)? No

After finishing all the steps the nextjs will be installed successfully. Now we can proceed for how to structure our application for making it into server side.


The root file should always be on server side for making any nextjs application completely on server side and from root file i mean the page.tsx that is present inside app directory. This is the very important point that you need to take care about because the nextjs follows the tree wise hierarchy so if you root file becomes the client side the entire application will be run on client side. There are some points you need to take care about before building server side nextjs application you can look for them bellow:-

 1. Use "use server" on every page.tsx
 2. While building server side application you cannot use interactivity and event listeners (`onClick()`, `onChange()`, etc)
 3. You cannot use State and Lifecycle Effects (`useState()`, `useReducer()`, `useEffect()`, etc)
 4. You cannot use custom hooks that depend on state, effects, or browser-only APIs

Now suppose if you are designing any component that requires you to use any lifecycle effect or event listeners then for that you can create a seperate file on client side and use "use client" into it. This will prevent the whole page to be on client side just the part of the code will be on client side and this is allowed also.

Just remember the root file should always be on server side the subsequent file that are directly associated with the root file are also to be on server side and from server side i mean the above mentioned points to be take care.
If you want to check whether you current page that you build is on server side or client side just simply put a console log into it and if you could see your reponse on the editor terminal then you are going corrent but if you see the result on browser console then the application is running on client side

