public class Utils
{
    public static void printPrompt(String motADeviner, int tentatives, int tentativesMax, String lettresTrouvees)
    {
        // Effacer l'écran de manière compatible Windows
        try
        {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        }
        catch (Exception e)
        {
            // En cas d'échec, on affiche plusieurs lignes vides
            for (int i = 0; i < 50; i++)
            {
                System.out.println();
            }
        }

        String motADevinerMasque = "";

        String prompt = "-------------------------------------------------\n\n";

        for (int i = 0; i < motADeviner.length(); i++)
        {
            if (lettresTrouvees.contains(String.valueOf(motADeviner.charAt(i))))
            {
                motADevinerMasque += motADeviner.charAt(i);
            }
            else
            {
                motADevinerMasque += "_";
            }
        }

        prompt += "Mot à deviner: " + motADevinerMasque + "\n";
        prompt += "Tentatives: " + tentatives + " / " + tentativesMax + "\n";
        prompt += "Tentatives restantes: " + (tentativesMax - tentatives) + "\n";
        prompt += "Lettres trouvées: " + lettresTrouvees + "\n\n";
        prompt += "-------------------------------------------------\n";
        prompt += "Veuillez entrer une lettre ou 'quit' pour quitter: ";

        System.out.print(prompt);
    }
}
