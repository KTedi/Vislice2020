% import model

<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

  <h2> {{ igra.pravilni_del_gesla() }} </h2>

  Nepravilni ugibi: <b> {{ igra.nepravilni_ugibi() }} </b> <br>

    <img src="/img/{{ igra.stevilo_napak() }}.jpg" alt="obesanje">

  % if stanje == model.ZMAGA:

  <h3> Čestitam. Uspelo ti je. </h3>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % elif stanje == model.PORAZ:

  <h3> Ni ti uspelo. </h3>

  Pravilno geslo je bilo: <b> {{ igra.geslo }} </b>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else: 

  <form action="/igra/" method="post">
     Črka: <input type= "text" name="crka" maxlength="1">
     <button type="submit">Nova igra</button>
  </form>

    % end

</body>

</html>