def determine_tb_drug_resistance(drug_list):
    """
    Determines the type of drug resistance in tuberculosis (TB) based on the given list of drugs.

    Args:
    - drug_list (list): List of drugs to check for resistance.

    Returns:
    - resistance_type (str): Type of drug resistance (HR-TB, RR-TB, MDR TB, pre-XDR TB, XDR TB, Sensitive, or other).
    """

    isoniazid = ['isoniazid']
    rifampicin = ['rifampicin']
    fluoroquinolones = ['ofloxacin', 'moxifloxacin', 'levofloxacin', 'ciprofloxacin', 'norfloxacin', 'gatifloxacin', 'gemifloxacin', 'sparfloxacin', 'pefloxacin', 'trovafloxacin']
    second_line_injectables = ['amikacin', 'kanamycin', 'capreomycin']
    group_a = ['levofloxacin', 'moxifloxacin', 'bedaquiline','linezolid']

    if all(drug in drug_list for drug in isoniazid) and all(drug in drug_list for drug in rifampicin):
        if all(drug in drug_list for drug in fluoroquinolones) and all(drug in drug_list for drug in group_a):
            return ['XDR-TB']
            # return ['MDR-TB']
        elif all(drug in drug_list for drug in fluoroquinolones)and all(drug in drug_list for drug in group_a):
            # return ['MDR-TB']
            return ['pre-XDR-TB']
        else:
            return ['MDR-TB']
    elif all(drug in drug_list for drug in isoniazid):
        return ['HR-TB']
    elif all(drug in drug_list for drug in rifampicin):
        return ['RR-TB']
    elif not drug_list:
        return ['Sensitive']
    else:
        print(drug_list)
        return ['other']
    
        # return [f'other:{drug_list}'] #! This used to output specific drug resistance, but now it just outputs 'other'.