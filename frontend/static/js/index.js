function create_square() {
    for (let i = 1; i <= 9; i++) {
        var elem = document.createElement('div');
        elem.className = "bigsquare";
        elem.id = "test".concat(i);
        elem.type = "text";
        for (let j = 1;j <= 9; j++) {
            var smallsquare = document.createElement('input');
            smallsquare.className = "smallsquare";
            smallsquare.id = j + 9 * (i - 1);
            smallsquare.type = "text";
            smallsquare.name = "testing" + (j + 9 * (i - 1));
            elem.appendChild(smallsquare);
        }


        document.getElementById("board").appendChild(elem);
    }
}

function square_fill_initially(coords) {
    for (id in coords) {
        document.getElementById(id).value = coords[id];
    }
}