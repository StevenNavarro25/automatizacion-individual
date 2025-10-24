import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Configurar navegador
driver = webdriver.Chrome()
driver.get("https://ecosistemaprov.unp.gov.co/oapi/gsc/formulario-individual")  # URL de tu front


def tab_and_action(driver, n_tabs, action=None, text=None, file_path=None):
    """Mueve el foco con n_tabs y realiza una acción.
       action = "enter" para presionar Enter
       text = string para escribir en el campo
    """
    for _ in range(n_tabs):
        driver.switch_to.active_element.send_keys(Keys.TAB)
    
    active = driver.switch_to.active_element

    if action == "file" and file_path:
        active.send_keys(file_path)
    elif text:
        driver.switch_to.active_element.send_keys(text)
    elif action == "enter":
        driver.switch_to.active_element.send_keys(Keys.ENTER)


# Leer datos desde CSV
with open('datos.csv', newline='', encoding='utf-8') as csvfile:
    lector = csv.DictReader(csvfile)
    for fila in lector:

        wait = WebDriverWait(driver, 10)

        # Esperar modal visible
        modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog")))

        # Click en botón dentro del modal
        boton = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'modal-dialog')]//button[contains(., 'Continuar')]")
        ))
        boton.click()

        # Esperar a que el modal desaparezca
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-dialog")))

        # Pais dilegenciamiento
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'País')]/following-sibling::select)[1]")
        select = Select(campo)
        select.select_by_visible_text("Colombia")

        # Departamento diligenciamiento
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//label[contains(text(), 'Departamento')]/following-sibling::select)[1]")))
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'Departamento')]/following-sibling::select)[1]")
        # Esperar a que la opción esté presente
        select = Select(campo)
        select.select_by_value(fila["departamento_domicilio"])

        # Municipio diligenciamiento
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//label[contains(text(), 'Municipio / Ciudad')]/following-sibling::select)[1]")))
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'Municipio / Ciudad')]/following-sibling::select)[1]")
        # Esperar a que la opción esté presente
        select = Select(campo)
        select.select_by_value(fila["municipio_domicilio"])

        # Primer nombre
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Primer nombre')]/following-sibling::input")
        campo.send_keys(fila["primer_nombre"])

        # Segundo nombre
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Segundo nombre')]/following-sibling::input")
        campo.send_keys(fila["segundo_nombre"])

        # Primer apellido
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Primer apellido')]/following-sibling::input")
        campo.send_keys(fila["primer_apellido"])

        # Segundo apellido
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Segundo apellido')]/following-sibling::input")
        campo.send_keys(fila["segundo_apellido"])

        # Sexo
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Sexo')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text(fila["sexo"])  # selecciona por texto visible

        # Tipo de identificacion
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Tipo de identificación')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text(fila["tipo_identificacion"])

        # Numero de identificacion
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Número de identificación')]/following-sibling::input")
        campo.send_keys(fila["numero_identificacion"])

        # Fecha de expedición
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Fecha de expedición')]/following-sibling::input")
        campo.send_keys("21-3-2025")

        # Fotocopia del documento de identificación personal
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Fotocopia del documento de identificación personal')]/following-sibling::input[@type='file']")
        campo.send_keys("C:\\Users\\Steven\\Downloads\\documento.pdf")

        # Pais nacimiento
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'País')]/following-sibling::select)[2]")
        select = Select(campo)
        select.select_by_visible_text("Colombia")

        # Departamento nacimiento
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//label[contains(text(), 'Departamento')]/following-sibling::select)[2]")))
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'Departamento')]/following-sibling::select)[2]")
        # Esperar a que la opción esté presente
        select = Select(campo)
        select.select_by_value(fila["departamento_domicilio"])
    
        # Municipio nacimiento
        # Esperar a que el select esté presente
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//label[contains(text(), 'Municipio / Ciudad')]/following-sibling::select)[2]")))
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'Municipio / Ciudad')]/following-sibling::select)[2]")
        select = Select(campo)
        select.select_by_value(fila["municipio_domicilio"])

        # Fecha de nacimiento
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Fecha de nacimiento')]/following-sibling::input")
        campo.send_keys("21-8-2005")

        # Pais de domicilio
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'País')]/following-sibling::select)[3]")
        select = Select(campo)
        select.select_by_visible_text("Colombia")

        # Departamento domicilio
        time.sleep(2)
        # Esperar a que el select esté presente
        wait.until(EC.presence_of_element_located((By.XPATH, "(//label[contains(text(), 'Departamento')]/following-sibling::select)[3]")))
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'Departamento')]/following-sibling::select)[3]")
        select = Select(campo)
        select.select_by_value(fila["departamento_domicilio"])
    
        # Municipio domicilio
        time.sleep(2)
        # Esperar a que el select esté presente
        wait.until(EC.presence_of_element_located((By.XPATH, "(//label[contains(text(), 'Municipio / Ciudad')]/following-sibling::select)[3]")))
        campo = driver.find_element(By.XPATH, "(//label[contains(text(), 'Municipio / Ciudad')]/following-sibling::select)[3]")
        select = Select(campo)
        select.select_by_value(fila["municipio_domicilio"])

        # Zona de domicilio
        if fila["zona_domicilio"] == "Urbano":
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Zona')]/following-sibling::select")
            select = Select(campo)
            select.select_by_visible_text("Urbano")

            # Via principal
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Vía principal')]/following-sibling::select")
            select = Select(campo)
            select.select_by_visible_text("Carrera")

            # Número vía
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Número vía')]/following-sibling::input")
            campo.send_keys(fila["numero_via"])

            # Número uno
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Número uno')]/following-sibling::input")
            campo.send_keys(fila["numero_uno"])

            # Letra
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Letra')]/following-sibling::input")
            campo.send_keys(fila["letra"])

            # Número dos
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Número dos')]/following-sibling::input")
            campo.send_keys(fila["numero_dos"])

            # Barrio / Sector
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Barrio / Sector')]/following-sibling::input")
            campo.send_keys(fila["barrio_sector"])

            # Indicaciones
            tab_and_action(driver, 1, text="Sin indicaciones")

        else:
            campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Zona')]/following-sibling::select")
            select = Select(campo)
            select.select_by_visible_text("Rural")

            # Corregimiento
            tab_and_action(driver, 1, text="San Antonio")

            # Vereda
            tab_and_action(driver, 1, text="Soacha")

            # Indicaciones lugar domicilio
            tab_and_action(driver, 2, text="Cerca de la iglesia muy por fuera de bogota y mas")

        # Celular uno
        tab_and_action(driver, 1, text=fila["celular_uno"])

        # Correo
        tab_and_action(driver, 3, text=fila["correo"])  

        # Botón continuar
        tab_and_action(driver, 3, action="enter")

        # Genero
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Género')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text(fila["genero"])

        # Orientacion sexual
        tab_and_action(driver, 1, text=fila["orientacion_sexual"])

        # Factor diferencial
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Factor diferencial')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text("Cuidador / Cuidadora")

        tab_and_action(driver, 1, text=fila["personas_cargo"])

        # Tipo de discapacidad
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Tipo discapacidad')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text(fila["discapacidad"])

        # Grupo etnico
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Grupo étnico')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text("Indígena")

        # Etnia
        tab_and_action(driver, 1, text="Kasmatarrua")

        # Resguardo
        tab_and_action(driver, 1, text="Cristisania")

        # Comunidad
        tab_and_action(driver, 1, text="Embera Chamí")

        # Parcialidad
        tab_and_action(driver, 1, text="Embera")

        # Comunidad
        tab_and_action(driver, 1, text="Resguardo Indigena")

        # Tipo de organizacion
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Tipo de organización')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text("Social")

        # Nombre de la organizacion
        tab_and_action(driver, 1, text="Asociación de Prueba")

        # Numero identificacion
        tab_and_action(driver, 2, text="123456789")

        # Medida cautelar o provisional 
        campo = driver.find_element(By.XPATH, "//label[contains(text(), 'Medida cautelar o provisional')]/following-sibling::select")
        select = Select(campo)
        select.select_by_visible_text("Medida Cautelar otorgada por un juez de la República")

        # Acciones a favor del medioambiente
        tab_and_action(driver, 1)  
        if not driver.switch_to.active_element.is_selected():
            driver.switch_to.active_element.send_keys(Keys.SPACE)
            time.sleep(0.5)

        # Búsqueda de personas dadas por desaparecidas
        checkbox = driver.find_element(
            By.XPATH,
            "//label[contains(., '¿Es usted mujer buscadora de víctimas de desaparición forzada?')]/following-sibling::div//input[@type='checkbox']"
        )

        # Validar si está habilitado
        if checkbox.is_enabled():
            if not checkbox.is_selected():
                checkbox.send_keys(Keys.SPACE)  # Activar con tecla ESPACIO
                time.sleep(0.5)

        # Botón continuar
        # Hacer scroll al body antes de continuar
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Buscar el botón
        boton_siguiente = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Siguiente')]")))

        # Mover el foco dinámicamente con JS
        driver.execute_script("arguments[0].focus();", boton_siguiente)
        boton_siguiente.send_keys(Keys.ENTER)

        # Hacer click en el body antes de seguir tabulando
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Nombre tercero
        tab_and_action(driver, 2, text=fila["nombre_tercero"]) 

        # Apellido tercero
        tab_and_action(driver, 2, text=fila["apellido_tercero"]) 

        # Celular uno tercero
        tab_and_action(driver, 2, text=fila["celular_uno_tercero"]) 

        # Correo tercero
        tab_and_action(driver, 3, text=fila["correo_tercero"]) 

        # Botón continuar
        tab_and_action(driver, 2, action="enter")
        time.sleep(0.5)

         # Hacer click en el body antes de seguir tabulando
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Situación de amenaza
        tab_and_action(driver, 1)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        tab_and_action(driver, 2)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        # Medio por el que se presentó
        tab_and_action(driver, 5)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        tab_and_action(driver, 2)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        tab_and_action(driver, 3)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        # Relato de los hechos generadores de la situación de amenaza
        tab_and_action(driver, 1, text="Describa de forma breve y haciendo claridad en su relato del tiempo, modo y lugar de los hechos ocurridos recientemente, que le generan la posible situación de amenaza, y que correspondan a circunstancias constitutivas de afectación a los derechos fundamentales a la vida, libertad, seguridad e integridad.")

         # Evidencia(s) de la situación o amenaza
        tab_and_action(driver, 1, action="file", file_path=r"C:\Users\Steven\Downloads\Anexo.pdf")
        time.sleep(0.5)

        # Boton siguiente
        boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Siguiente')]")))
        # Hacer scroll al botón antes de hacer clic
        driver.execute_script("arguments[0].scrollIntoView(true);", boton)
        try:
            boton.click()
        except Exception:
            # Si el clic es interceptado, usar JavaScript
            driver.execute_script("arguments[0].click();", boton)

        # Hacer click en el body antes de seguir tabulando
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Poblaciones del Programa de Prevención y Protección de los derechos a la vida, la libertad, la integridad y la seguridad de personas
        tab_and_action(driver, 1)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        tab_and_action(driver, 2)
        select = Select(driver.switch_to.active_element)
        select.select_by_visible_text("Nacional")

        tab_and_action(driver, 1)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        tab_and_action(driver, 1, text="Lider del campo")

        tab_and_action(driver, 1)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        tab_and_action(driver, 1)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        # Acreditación a la población objeto
        tab_and_action(driver, 16, action="file", file_path=r"C:\Users\Steven\Downloads\documentopoblacion.pdf")
        time.sleep(0.5)

        # Boton siguiente
        boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Siguiente')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", boton)
        time.sleep(0.5)  # darle chance al scroll
        boton.click()


        # Hacer click en el body antes de seguir tabulando
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Términos y Condiciones de la Política de Tratamiento de Datos Personales de la UNP
        tab_and_action(driver, 3)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        # Medidas preventivas por parte de la Policía Nacional
        tab_and_action(driver, 3)  
        driver.switch_to.active_element.send_keys(Keys.SPACE)

        # ¿El formulario es diligenciado por el solicitante?
        # Encuentra el label por su texto
        label = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(., '¿El formulario es diligenciado por el solicitante?')]")
        ))

        # Encuentra el checkbox que está en el div siguiente al label
        checkbox = label.find_element(By.XPATH, "./following-sibling::div//input[@type='checkbox']")

        # Hacer scroll hasta el checkbox
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)

        # Enfocar y activar con tecla ESPACIO
        checkbox.send_keys(Keys.SPACE)

        boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Enviar')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", boton)
        time.sleep(0.5)  # pequeño delay para que termine el scroll
        boton.click()

        # Esperar un poco antes de la siguiente iteración
        time.sleep(6)
        # Recargar la página para volver a llenar el formulario
        driver.get("https://ecosistemaprov.unp.gov.co/oapi/gsc/formulario-individual")

        # Esperar un poco antes de la siguiente iteración
        time.sleep(2)
        
# Cerrar navegador
driver.quit()