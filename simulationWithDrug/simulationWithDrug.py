def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb,
                       resistances, mutProb, numTrials):
    # TODO
    for trial in range(numTrials):
        (totalVirusResult, resistantVirusResult) = runTrial2(150, 150, numViruses,
                                                             maxPop, maxBirthProb,
                                                             clearProb, resistances,
                                                             mutProb)

        if trial == 0:  # First trial
            # Save results of the first trial...
            totalVirusPop = totalVirusResult
            resistantVirusPop = resistantVirusResult
        else:
            # ...then accumulate second and subsequent sets
            for i in range(len(totalVirusResult)):
                totalVirusPop[i] += totalVirusResult[i]
                resistantVirusPop[i] += resistantVirusResult[i]

    # End of the numTrial trials. Average the results accumulated during
    # the trials over the number of trials. (See HINT in problem spec.)
    for i in range(len(totalVirusPop)):
        totalVirusPop[i] /= float(numTrials)
        resistantVirusPop[i] /= float(numTrials)

    # PLOT THE RESULTS OF THE SIMULATION AS TWO PLOTS
    # Let X-axis scale default to length of Y-values lists (300)
    # Here is how we deal with plotting two sets of y-values
    pylab.plot(totalVirusPop, label = 'Total virus population') 
    pylab.plot(resistantVirusPop, label = 'Resistant virus population')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time step')
    pylab.ylabel('# viruses')
    pylab.legend(loc = 'best')
    pylab.show()
    
def runTrial2(numTimeSteps1, numTimeSteps2, numViruses, maxPop,
              maxBirthProb, clearProb, resistances, mutProb):

    # Create numViruses virus instances with specified:
    #   maxBirthProb 
    #   clearProb
    #   resistances
    #   mutProb
    # attribute values
    viruses = []
    for virus in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

    # Instantiate a patient with the list of numVirus virus instances
    # and a Maximum Sustainable Virus Population of maxPop
    patientInst = TreatedPatient(viruses, maxPop)  # one line of code

    # Simulate changes to the virus population over elapsedTimeSteps
    # steps.
    # The patient has numViruses virus level at start.

    allVirusLevelsThisTrial = []
    resistantVirusLevelsThisTrial = []
    # Record starting level of viruses in patient...
    # NO! See the BEWARE! comments above..
    #REMOVE LINE# allVirusLevelsThisTrial.append(...)  # total virus...
    #REMOVE LINE# resistantVirusLevelsThisTrial.append(...) # resistant virus...

    # Record virus population changes over numTimeSteps1 
    # number of updates. Do the update first then record the
    # two virus populations of interest that results.
    for timestep in range(numTimeSteps1):
        newVirusLevels = patientInst.update()
        allVirusLevelsThisTrial.append(patientInst.getTotalPop()) # use the getter method
        # Note below, looking at virus population resistant to 'guttagonol'
        resistantVirusLevelsThisTrial.append(patientInst.getResistPop(['guttagonol'])) # use the getter method

    # Add the drug 'guttagonol' to the patient and run a further
    # numTimeSteps2 number of updates
    patientInst.addPrescription('guttagonol')
    for timestep in range(numTimeSteps2):
        newVirusLevels = patientInst.update()
        allVirusLevelsThisTrial.append(patientInst.getTotalPop()) # use the getter method
        # Note below, looking at virus population resistant to 'guttagonol'
        resistantVirusLevelsThisTrial.append(patientInst.getResistPop(['guttagonol'])) # use the getter method

    return (allVirusLevelsThisTrial, resistantVirusLevelsThisTrial)
    
