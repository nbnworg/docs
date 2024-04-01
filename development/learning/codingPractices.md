# Coding Standards at NBNW
Live CR Session 1 - https://youtu.be/fLotOp2v8r8

## 1. Purpose
This document outlines the coding practices that every developer, be it MLE, SDE, Data Analytics Engineer, etc has to follow. Any Role that ends with Engineer at NBNW will have to read this document and adhere to the standards.

## 2. Key things to Remember while coding
1. You are not working on a Project, it is the company itself that you are building.
2. You HAVE to build reusable things, DON'T develop for yourself.
3. Remember that there are other people who will be taking over your code. Keep the style consistent.

## 3. Developer Habit
Since you have been hired at NBNW, it means you displayed potential. Potential strong enough to prove that you are one of the best developer there is.

To maintain that, you SHOULD have the following traits as a developer.

1. If you see something wrong, FIX IT!
2. If you see something inconsistent, you should feel a strong detestment towards it.
3. If you feel detestment towards something, fix it.
4. You should avoid repeating things, if something is repeated, generalize it.
5. You should be self sufficient to solve the issues and learn new things.
6. You should intuitively realize if the standards are getting low AND DO SOMETHING TO RAISE THEM.


## 4. What not to do

### 4.1 Do a commit that has commented out code
People like to keep commented out code in the repository. That is strictly forbidden at NBNW. We do not have commented out code in our repository regardless of circumstances.

Keep in mind, you are not developing for yourself but for others. Commented out code makes it difficult for others to understand and brings this question - "IS IT NEEDED?"

e.g. of bad practice -
```

//     {
//       name: "YouTube",
//       href: "#",
//       icon: (props: JSX.IntrinsicAttributes & SVGProps<SVGSVGElement>) => (
//         <svg fill="currentColor" viewBox="0 0 24 24" {...props}>
//           <path
//             fillRule="evenodd"
//             d="M19.812 5.418c.861.23 1.538.907 1.768 1.768C21.998 8.746 22 12 22 12s0 3.255-.418 4.814a2.504 2.504 0 0 1-1.768 1.768c-1.56.419-7.814.419-7.814.419s-6.255 0-7.814-.419a2.505 2.505 0 0 1-1.768-1.768C2 15.255 2 12 2 12s0-3.255.417-4.814a2.507 2.507 0 0 1 1.768-1.768C5.744 5 11.998 5 11.998 5s6.255 0 7.814.418ZM15.194 12 10 15V9l5.194 3Z"
//             clipRule="evenodd"
//           />
//         </svg>
//       ),
//     },
//   ],
// };

export default function About() {
```

You'd argue that we can use this later. We will make it, when we will use it. Code Repository is no place for you to be adding that.


### 4.2 Go out of pattern
There are multiple ways in which you can go out of pattern some examples are -
1. Going out of pattern for repository structure (e.g. All components are inside components folder, you place a page, e.g. About inside the component folder as well)
2. Going out of pattern for naming (e.g. For any component, lets say we have same name component defined inside as the file name. For a new one, you change that...)
3. Going out of pattern for toolset being used (e.g. We are using Tailwind CSS for every styling piece, you find it difficult and change to use the normal one instead. DONT DO THAT.)
4. Going out of pattern for naming convention (e.g. say you have everything named in camel case e.g. someCoolName, for some variable you name it as some_stupid_variable, Don't do that)

As you can see, there are many ways in which you can go out of being consistent with the existing pattern. Make sure to thoroughly review the code repository that you will be working on and understand the pattern for the same.

### 4.3 Do unnecessary changes
Sometimes, the commits might have more things than necessary, this adds silent bugs.

See the below commits - 
From - 
```
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React + TS</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```
To - 
```
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/svg+xml+png" href="/nbnw2-no-bg.png" />
  <meta name=" viewport" content="width=device-width, initial-scale=1.0" />
  <title>NBNW</title>
</head>

<body>
  <div id="root"></div>
  <script type="module" src="/src/main.tsx"></script>
</body>
</html>
```

Notice that there was a space added in "viewport" which created a silent bug for mobile devices that didn't rendered the website properly.

### 4.4 Have comments
Comments should be avoided. We should have minimum comments. We should only be having comments that talks about the purpose of a particular block and not what it is.

Some sample useless comments are - 
```
// Increased size for extraLarge
    default:
      return "md:w-1/2 lg:w-1/3";
```

```
// Make sure to destructure `isActive` from props
export default function RectangleButton({
  text,
  onClick,
```

```
// Assuming these components are defined elsewhere in your project
import RectangleButton from "../buttons/rectangleButton";
```
```
categories={categories} // Pass categories
handleCategoryClick={handleCategoryClick} // Pass click handlertoggleSidenav={handleToggleSidenav} // Pass toggle function
```


Notice that for some, you can even realize that ChatGPT comments are added alongside. It is not a good practice to have them in your commits either.



### 4.5 Hardcoding Values
You should be maintaining constant files where we are using them in more than once place or you expect frequent changes.

People generally do things centric to what they are solving and fail to see the bigger picture. 

See the bad example below - 
```
    <li>
    <RectangleButton
    text="Technology"
    onClick={() => handleCategoryClick("Technology")}
    isActive={categories.includes("Technology")}
    />
    </li>
    <li>
    <RectangleButton
    text="Fashion"
    onClick={() => handleCategoryClick("Fashion")}
    isActive={categories.includes("Fashion")}
    />
    </li>
    <li>
    <RectangleButton
    text="Opinion"
    onClick={() => handleCategoryClick("Opinion")}
    isActive={categories.includes("Opinion")}
    />
    </li>
    <li>
    <RectangleButton
    text="World"
    onClick={() => handleCategoryClick("World")}
    isActive={categories.includes("World")}
    />
    </li>
```

See the good example below - (we moved CATEGORIES to constant file and use that, this was then also used for dropdown!)
```
{
CATEGORIES.map((item) => (
    <li>
    <RectangleButton
    text={item}
    onClick={() => handleCategoryClick(item)}
    isActive={categories.includes(item)}
    />
</li>
))
}
```



## 5. Bad Examples
[TODO] add review examples here.
