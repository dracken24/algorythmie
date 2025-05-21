/* =============================================================================== */
/* ---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~--- */
/*               -------------------------------------------------                 */
/*                PROJET: Java Dev          PAR: Dracken24                         */
/*               -------------------------------------------------                 */
/*                CREATED: 21-5th-2025                                             */
/*                MODIFIED BY: Dracken24                                           */
/*                LAST MODIFIED: 21-5th-2025                                       */
/*               -------------------------------------------------                 */
/*                FILE: Core.java                                                  */
/*               -------------------------------------------------                 */
/* ---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~--- */
/* =============================================================================== */

public class Core
{
    boolean running;
    String motADeviner;
    String lettresTrouvees;
    int tentatives;
    int tentativesMax;

    Core()
    {
        running = true;
        motADeviner = "avion";
        tentatives = 0;
        tentativesMax = 6;
        lettresTrouvees = "";
    }

    public void Start()
    {
        
    }

    public void Update()
    {
        Utils.printPrompt(motADeviner, tentatives, tentativesMax, lettresTrouvees);

        KeyGestion();

        if (tentatives >= tentativesMax)
        {
            System.out.println("\nVous avez perdu ! Le mot était : " + motADeviner);
            System.out.println("Appuyez sur 'enter' pour quitter.");
            
            System.console().readLine();
            
            Stop();
        }
    }

    public void Stop()
    {
        running = false;
    }

    public void KeyGestion()
    {
        String key = System.console().readLine();

        if (key.equals("quit"))
        {
            Stop();
            return;
        }
        else if (key.length() != 1 || !Character.isLetter(key.charAt(0)))
        {
            System.out.println("Veuillez entrer une lettre valide.");
            Wait(1500);
            return;
        }

        if (motADeviner.contains(key))
        {
            for (int i = 0; i < motADeviner.length(); i++)
            {
                if (motADeviner.charAt(i) == key.charAt(0))
                {
                    for (int j = 0; j < motADeviner.length(); j++)
                    {
                        if (motADeviner.charAt(j) == key.charAt(0))
                        {
                            lettresTrouvees += key;
                            tentatives++;
                            System.out.println("\n--- Lettre correcte ! ---\n");

                            Wait(1500);
                        }
                    }
                }
            }
        }
        else
        {
            if (!lettresTrouvees.contains(key))
            {
                lettresTrouvees += key;
                tentatives++;

                System.out.println("\n--- Lettre incorrecte ! ---\n");

                Wait(1500);
            }
        }
    }

    public void Wait(int ms)
    {
        try
        {
            Thread.sleep(ms);
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }
    }
}
