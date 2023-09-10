<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Check</title>
    <style>

    body{
            background-color: black;
        }
    h1{
        color: white;
        font-family: monospace;
        text-shadow: 1px 0.5px rgb(124, 245, 253);

    }

    
    #cont{

        display: flex;
        justify-content: center;
        margin-top: 100px;
        

    }

    input{
        border: none;
        border-bottom: 3px solid #283246 !important;
        font-family: sans-serif;
        width: 298px;
        height: 35px;
        
        

    }
    button{
        display: inline-block;
        position: relative;
        background: none;
        color: #fff;
        cursor: pointer;
        font-size: 30px;
        font-family: monospace;
        width: 200px;
        height: 60px;
        
    }

    span{
    display: block;
    padding: 5px 1px;
    }
    button::before, button::after{
    content:"";
    width: 0;
    height: 2px;
    position: absolute;
    transition: all 0.2s linear;
    background: #fff;

    }

    span::before, span::after{
    content:"";
    width:2px;
    height:0;
    position: absolute;
    transition: all 0.2s linear;
    background: #fff;
    
    }
    button:hover::before, button:hover::after{
    width: 100%;
    }
    button:hover span::before, button:hover span::after{
    height: 100%;
    }
    /*----- button 1 -----*/
    .btn-1::before, .btn-1::after{
    transition-delay: 0.2s;
    }
    .btn-1 span::before, .btn-1 span::after{
    transition-delay: 0s;
    }
    .btn-1::before{
    right: 0;
    top: 0;
    }
    .btn-1::after{
    left: 0;
    bottom: 0;
    }
    .btn-1 span::before{
    left: 0;
    top: 0;
    }
    .btn-1 span::after{
    right: 0;
    bottom: 0;
    }
    .btn-1:hover::before, .btn-1:hover::after{
    transition-delay: 0s;
    }
    .btn-1:hover span::before, .btn-1:hover span::after{
    transition-delay: 0.2s;
    }



 .material {
         position: relative;
         padding: 0;
         margin: 5px;
         border: none;
         overflow: visible;
}
 .material input {
         box-sizing: border-box;
         width: 100%;
         padding: 12px 10px 8px;
         border: none;
         border-radius: 0;
         box-shadow: none;
         border-bottom: 1px solid #ddd;
         font-size: 120%;
         outline: none;
         cursor: text;
}
 .material input::-webkit-input-placeholder {
         transition: color 300ms ease;
}
 .material input:not(:focus)::-webkit-input-placeholder {
         color: transparent;
}
 .material hr {
         content: '';
         display: block;
         position: absolute;
         bottom: 0;
         left: 0;
         margin: 0;
         padding: 0;
         width: 100%;
         height: 2px;
         border: none;
         background: #607d8b;
         font-size: 1px;
         will-change: transform, visibility;
         transition: all 200ms ease-out;
         transform: scaleX(0);
         visibility: hidden;
         z-index: 10;
}
 .material input:focus ~ hr {
         transform: scaleX(1);
         visibility: visible;
}
 .material label {
         position: absolute;
         top: 10px;
         left: 10px;
         font-size: 120%;
         color: #607d8b;
         transform-origin: 0 -150%;
         transition: transform 300ms ease;
         pointer-events: none;
}

 h2{

     text-align: center;
     color: whitesmoke;
     font-family: monospace;
     font-size: 60px;
     text-shadow: 1px 3px rgb(124, 245, 253);
 }

 h3{
     color: whitesmoke;
     font-family: monospace;
     text-align: center;
     font-size: 30px;
     text-shadow: 1px 1px rgb(223, 216, 125);
 }

    </style>
</head>
<body>

<h2>𝒸𝓱è𝓬k</h2>
<div id="cont">
    <form action="check.php" method="POST">
        <h1>password</h1>
        <input type="text" name="password" id="password">
        <button class="btn-1"><span>Check:)</span></button>
    </form>
</div>
<?php 
  if($_SERVER["REQUEST_METHOD"] == "POST"){
    $pwd = $_POST["password"];

    if ($pwd === "sadsau" ){

        echo "<h3>Nice: PCTF{Y0u_Ch3k3d_1t_N1c3lY_149}</h3>";
    }
    else{
        echo "<h3>incorrect password</h3>";
    }
  }
?>
</body>

