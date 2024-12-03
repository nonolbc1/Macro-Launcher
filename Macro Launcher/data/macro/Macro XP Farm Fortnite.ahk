; AutoHotkey v2

; Démarre une boucle avec un timer
SetTimer(MacroActions, 30000)

; Associer CTRL+F4 à la fermeture du script
^F4::ExitApp  ; Ferme ce script lorsque CTRL+F4 est pressé

; Définition de la fonction pour les actions
MacroActions() {
    Send("z")           ; Appuie sur Z
    Sleep(2000)         ; Attend 2 secondes
    Send("{Space}")     ; Appuie sur Espace
    Sleep(100)          ; Pause courte
    Send("s")           ; Appuie sur S
    Sleep(2000)         ; Attend 2 secondes
}