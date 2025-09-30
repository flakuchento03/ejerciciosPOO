// Clase Alumno
class Alumno {
  constructor(nombre, edad, calificaciones) {
    this.nombre = nombre;
    this.edad = edad;
    this.calificaciones = calificaciones;
  }

  // Métodos
  promedio() {
    let sum = this.calificaciones.reduce((a, b) => a + b, 0);
    return (sum / this.calificaciones.length).toFixed(2);
  }

  detalleHTML() {
    return `
      <div class="card">
        <h2>${this.nombre}</h2>
        <p><strong>Edad:</strong> ${this.edad}</p>
        <p><strong>Calificaciones:</strong> ${this.calificaciones.join(", ")}</p>
        <p><strong>Promedio:</strong> ${this.promedio()}</p>
      </div>
    `;
  }
}

// Clase App para manejar la UI
class App {
  constructor() {
    this.alumnos = [];
    this.cargarDatos();
  }

  async cargarDatos() {
    try {
      let resp = await fetch("data.json");
      let data = await resp.json();
      this.alumnos = data.map(a => new Alumno(a.nombre, a.edad, a.calificaciones));
    } catch (e) {
      console.error("Error al cargar datos:", e);
      document.getElementById("contenido").innerHTML = `
        <div class="card">
          <p style="color:red;">No se pudo cargar el archivo data.json</p>
        </div>
      `;
    }
  }

  mostrarLista() {
    const cont = document.getElementById("contenido");
    if (this.alumnos.length === 0) {
      cont.innerHTML = "<p>No hay alumnos cargados.</p>";
      return;
    }
    cont.innerHTML = "<h2>Lista de Alumnos</h2>";
    this.alumnos.forEach(al => {
      cont.innerHTML += `
        <div class="card">
          <h3>${al.nombre}</h3>
          <p>Edad: ${al.edad}</p>
        </div>
      `;
    });
  }

  mostrarDetalle() {
    const cont = document.getElementById("contenido");
    if (this.alumnos.length === 0) {
      cont.innerHTML = "<p>No hay alumnos disponibles.</p>";
      return;
    }
    cont.innerHTML = "<h2>Detalle del primer alumno</h2>";
    cont.innerHTML += this.alumnos[0].detalleHTML();
  }

  mostrarPromedio() {
    const cont = document.getElementById("contenido");
    if (this.alumnos.length === 0) {
      cont.innerHTML = "<p>No hay alumnos para calcular promedios.</p>";
      return;
    }
    cont.innerHTML = "<h2>Promedios de Alumnos</h2>";
    this.alumnos.forEach(al => {
      cont.innerHTML += `
        <div class="card">
          <h3>${al.nombre}</h3>
          <p>Promedio: ${al.promedio()}</p>
        </div>
      `;
    });
  }
}

// Instancia global
const app = new App();
