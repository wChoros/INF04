# Webowki
## Create react app
```bash
npx create-vite@latest
```

## Iterate over list elements on array

```js
{
    elements.map((element, id) => {
        return <li id={`element-${id}`}>{course}</li>
    })
}
```

## Prevent form reload
```js
<form onSubmit={(e) => { e.preventDefault(); handleSubmit(); }}>
```

