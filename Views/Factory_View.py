from PyQt5.QtWidgets import QMdiArea, QInputDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSlot
from Models.Layout import *
from Views import sub_win_factory

class Factory_View(QMdiArea):
    """description of class"""
    def __init__(self, fac_mdl, prod_mdl, mat_mdl, lay_ctrl, mat_ctrl, pro_ctrl):
        super().__init__()

        self._panel_factory = sub_win_factory.Ui_Form()
        self._panel_factory.setupUi(self)

        self._model_factory = fac_mdl
        self._model_product = prod_mdl
        self._model_material = mat_mdl
        self._controller_layout = lay_ctrl
        self._controller_material = mat_ctrl
        self._controller_product = pro_ctrl

        self.load_layout_pictures()
        self.update_lbls_fix_line_info()
        self.update_lbl_process_info()
        self.update_lbl_process_departments(False)
        self.update_lbl_cellular_info()
        self.update_lbl_cellular_departments(False)
        self.update_fac_tab1_midright_lbl(self._model_factory.nb_fixed_position, self._model_factory.nb_process, self._model_factory.nb_cellular, self._model_factory.nb_line)

        # connect to factory model
        self._model_factory.layout_nb_changed.connect(self.update_fac_tab1_midright_lbl)
        

    @pyqtSlot(str)
    def update_fac_tab1_top_lbl(self, text):
        self._panel_factory.lbl_top.setText(text)

    @pyqtSlot(int)
    def update_fac_tab1_midleft_lbl(self, size, free_size, total_cost, fixed_cost, cur_sign):
        self._panel_factory.lbl_mid_left.setText(f'Factory Size:\t{size} m\u00b2\nAvailable Space: \t{free_size} m\u00b2 \n\nTotal fixed Cost:\t{total_cost:,}{cur_sign} \nCost per m\u00b2:\t{fixed_cost:,}{cur_sign}')

    @pyqtSlot(int, int, int, int)
    def update_fac_tab1_midright_lbl(self, fix, pro, cell, line):
        self._panel_factory.lbl_mid_right.setText(f'Layouts\n\nFixed Position:\t{fix}\nProcess:\t\t{pro}\nCellular:\t\t{cell}\nLine:\t\t{line}')

    def update_lbls_fix_line_info(self):
        self._panel_factory.lbl_tab2_right.setText(f'Layout Effects\n\nProduction Time:\t{Fixed_Position_Layout.STANDARD_PROD_TIME_MODIFIER  * 100:.0f}%\
            \nMaintenance Cost p.m\u00b2:\t{Fixed_Position_Layout.STANDARD_COST_MODIFIER * 100:.0f}%\nQuality Factor:\t\t{Fixed_Position_Layout.STANDARD_QUALITY_MODIFIER}')
        self._panel_factory.lbl_tab2_left.setText(f'Requirements\n\nBuilding Cost:\t{Fixed_Position_Layout.BUILDING_COST:,}€\nBuilding Time:\t{Fixed_Position_Layout.BUILDING_TIME} turns\
            \nSpace:\t\t{Fixed_Position_Layout.STANDARD_SIZE} m\u00b2')
        self._panel_factory.lbl_tab5_right.setText(f'Layout Effects\n\nProduction Time:\t{Line_Layout.STANDARD_PROD_TIME_MODIFIER  * 100:.0f}%\nMaintenance Cost p.m\u00b2:\t{Line_Layout.STANDARD_COST_MODIFIER * 100:.0f}%')
        self._panel_factory.lbl_tab5_left.setText(f'Requirements\n\nBuilding Cost:\t{Line_Layout.BUILDING_COST:,}€\nBuilding Time:\t{Line_Layout.BUILDING_TIME} turns\
            \nSpace:\t\t{Line_Layout.STANDARD_SIZE} m\u00b2')

    def update_lbl_process_info(self):
        self._panel_factory.lbl_tab3_right.setText(f'Layout Effects\n\nProduction Time:\t{Process_Layout.STANDARD_PROD_TIME_MODIFIER  * 100:.0f}%\
            \nMaintenance Cost p.m\u00b2:\t{Process_Layout.STANDARD_COST_MODIFIER * 100:.0f}%\nQuality Factor:\t\t{Process_Layout.STANDARD_QUALITY_MODIFIER}')
        self._panel_factory.lbl_tab3_left.setText(f'Requirements\n\nBuilding Cost:\t{Process_Layout.BUILDING_COST:,}€\nBuilding Time:\t{Process_Layout.BUILDING_TIME} turns\
            \nSpace:\t\t{Process_Layout.STANDARD_SIZE} m\u00b2')

    def update_lbl_process_departments(self, flag, number_of_dept = Process_Layout.INIT_DEPARTMENTS, dept_size = Process_Layout.DEPARTMENT_SIZE,
    dept_time = Process_Layout.DEPARTMENT_BUILDING_TIME, dept_cost = Process_Layout.DEPARTMENT_BUILDING_COST, prod_bonus = Process_Layout.DEPARTMENT_PROD_BONUS):
        """Update nb of departments, size, building time and cost.
        if flag == true, takes actual numbers from existing layout."""
        if flag:
            number_of_dept, dept_size, dept_time, dept_cost, prod_bonus = self._controller_layout.collect_process_info()
        self._panel_factory.lbl_tab3_right_dept.setText(f'Departments:\t\t{number_of_dept}\nDepartment Size:\t{dept_size} m\u00b2\
            \nBuilding Time:\t\t{dept_time} month\nBuilding Cost:\t\t{dept_cost:,}€\nProduction Bonus:\t{prod_bonus * 100}%')

    def update_lbl_cellular_info(self):
        self._panel_factory.lbl_tab4_right.setText(f'Layout Effects\n\nProduction Time:\t{Cellular_Layout.STANDARD_PROD_TIME_MODIFIER  * 100:.0f}%\nMaintenance Cost p.m\u00b2:\t{Cellular_Layout.STANDARD_COST_MODIFIER * 100:.0f}%')
        self._panel_factory.lbl_tab4_left.setText(f'Requirements\n\nBuilding Cost:\t{Cellular_Layout.BUILDING_COST:,}€\nBuilding Time:\t{Cellular_Layout.BUILDING_TIME} turns\
            \nSpace:\t\t{Cellular_Layout.STANDARD_SIZE} m\u00b2')

    def update_lbl_cellular_departments(self, flag, number_of_dept = Cellular_Layout.INIT_DEPARTMENTS, dept_size = Cellular_Layout.DEPARTMENT_SIZE,
    dept_time = Cellular_Layout.DEPARTMENT_BUILDING_TIME, dept_cost = Cellular_Layout.DEPARTMENT_BUILDING_COST, prod_bonus = Cellular_Layout.DEPARTMENT_PROD_BONUS):
        """Update nb of departments, size, building time and cost.
        if flag == true, takes actual numbers from existing layout."""
        if flag:
            number_of_dept, dept_size, dept_time, dept_cost, prod_bonus = self._controller_layout.collect_cellular_info()
        self._panel_factory.lbl_tab4_right_dept.setText(f'Departments:\t\t{number_of_dept}\nDepartment Size:\t{dept_size} m\u00b2\
            \nBuilding Time:\t\t{dept_time} month\nBuilding Cost:\t\t{dept_cost:,}€\nProduction Bonus:\t{prod_bonus * 100}%')

    def build_fixed_pos_layout_clicked(self, free_space, funds, credit_limit = 10000):
        req_space = Fixed_Position_Layout.STANDARD_SIZE
        cost = Fixed_Position_Layout.BUILDING_COST
        cost_flag = True if cost <= funds + credit_limit else False
        space_flag = True if req_space <= free_space else False
        if cost_flag and space_flag:
            reply = QMessageBox.question(self, 'Expanding Production!', f'That will cost {cost:,}€ and take {Fixed_Position_Layout.BUILDING_TIME} months for completion. Are you sure?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            return True if reply == QMessageBox.Yes else False
        elif not cost_flag:
            self.show_message_funds(cost)
        elif not space_flag:
            self.show_message_space(req_space)
        return False

    def build_process_layout_clicked(self, free_space, funds, credit_limit = 10000):
        req_space = Process_Layout.STANDARD_SIZE
        cost = Process_Layout.BUILDING_COST
        cost_flag = True if cost <= funds + credit_limit else False
        space_flag = True if req_space <= free_space else False
        if cost_flag and space_flag:
            reply = QMessageBox.question(self, 'Expanding Production!', f'That will cost {cost:,}€ and take {Process_Layout.BUILDING_TIME} months for completion. Are you sure?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            return True if reply == QMessageBox.Yes else False
        elif not cost_flag:
            self.show_message_funds(cost)
        elif not space_flag:
            self.show_message_space(req_space)
        return False

    def build_cellular_layout_clicked(self, free_space, funds, credit_limit = 10000):
        req_space = Cellular_Layout.STANDARD_SIZE
        cost = Cellular_Layout.BUILDING_COST
        cost_flag = True if cost <= funds + credit_limit else False
        space_flag = True if req_space <= free_space else False
        if cost_flag and space_flag:
            reply = QMessageBox.question(self, 'Expanding Production!', f'That will cost {cost:,}€ and take {Cellular_Layout.BUILDING_TIME} months for completion. Are you sure?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            return True if reply == QMessageBox.Yes else False
        elif not cost_flag:
            self.show_message_funds(cost)
        elif not space_flag:
            self.show_message_space(req_space)
        return False

    def build_line_layout_clicked(self, free_space, funds, credit_limit = 10000):
        req_space = Line_Layout.STANDARD_SIZE
        cost = Line_Layout.BUILDING_COST
        cost_flag = True if cost <= funds + credit_limit else False
        space_flag = True if req_space <= free_space else False
        if cost_flag and space_flag:
            reply = QMessageBox.question(self, 'Expanding Production!', f'That will cost {cost:,}€ and take {Line_Layout.BUILDING_TIME} months for completion. Are you sure?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            return True if reply == QMessageBox.Yes else False
        elif not cost_flag:
            self.show_message_funds(cost)
        elif not space_flag:
            self.show_message_space(req_space)
        return False

    def increase_factory(self, build_cost, cur_sign, funds, credit_limit = 10000):
        """Opens Input dialog. Collects size (int) to add to factory size"""
        size, ok = QInputDialog.getText(self, 'Expand the Main Building?', 'How much more space do you want to build?')
        if ok:
            cost = int(size) * build_cost
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Building Bigger Hall!")
            msg.setInformativeText(f'That will cost you {cost:,}{cur_sign}. Are you sure?')
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                cost_flag = True if cost <= funds + credit_limit else False
                if cost_flag:
                    return int(size), cost
                else:
                    self.show_message_funds(cost)
                    return 0, 0
            elif retval == QMessageBox.Cancel:
                return 0, 0
        return 0, 0

    def delete_fixed_pos_layout(self):
         reply = QMessageBox.question(self, 'Dismantle Production!', f'Are you sure you want to dismantle one Fixed Position Layout?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
         if reply == QMessageBox.Yes:
             return True, 'Fixed Position Layout'
         else:
             return False, ''

    def delete_process_layout(self):
         reply = QMessageBox.question(self, 'Dismantle Production!', f'Are you sure you want to dismantle one Process Layout?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
         if reply == QMessageBox.Yes:
             return True, 'Process Layout'
         else:
             return False, ''

    def delete_cellular_layout(self):
         reply = QMessageBox.question(self, 'Dismantle Production!', f'Are you sure you want to dismantle one Cellular Layout?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
         if reply == QMessageBox.Yes:
             return True, 'Cellular Layout'
         else:
             return False, ''

    def delete_line_layout(self):
         reply = QMessageBox.question(self, 'Dismantle Production!', f'Are you sure you want to dismantle one Line Layout?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
         if reply == QMessageBox.Yes:
             return True, 'Line Layout'
         else:
             return False, ''

    def add_dept_process(self, free_space, funds, credit_limit = 10000):
        """Check if the player want and can build a new department.
        Returns the cost, if true. Else returns -1."""
        i = self._controller_layout.find_process_layout_index()
        if not i == -1:
            req_space = self._controller_layout._model_layout[i].department_size
            cost = self._controller_layout._model_layout[i].department_building_cost
            cost_flag = True if cost <= funds + credit_limit else False
            space_flag = True if req_space <= free_space else False
            if cost_flag and space_flag:
                reply = QMessageBox.question(self, 'Expanding Production!', f'That will cost {cost:,}€ and take {self._controller_layout._model_layout[i].department_building_time} months for completion. Are you sure?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self._controller_layout.add_department_process()
                    return cost, req_space
                else:
                    return -1, -1
            elif not cost_flag:
                self.show_message_funds(cost)
            elif not space_flag:
                self.show_message_space(req_space)
        else:
            self.show_message_not_found('Process Layout')
        return -1, -1

    def add_dept_cellular(self, free_space, funds, credit_limit = 10000):
        """Check if the player want and can build a new department.
        Returns the cost, if true. Else returns -1."""
        i = self._controller_layout.find_cellular_layout_index()
        if not i == -1:
            req_space = self._controller_layout._model_layout[i].department_size
            cost = self._controller_layout._model_layout[i].department_building_cost
            cost_flag = True if cost <= funds + credit_limit else False
            space_flag = True if req_space <= free_space else False
            if cost_flag and space_flag:
                reply = QMessageBox.question(self, 'Expanding Production!', f'That will cost {cost:,}€ and take {self._controller_layout._model_layout[i].department_building_time} months for completion. Are you sure?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self._controller_layout.add_department_celluluar()
                    return cost, req_space
                else:
                    return -1, -1
            elif not cost_flag:
                self.show_message_funds(cost)
            elif not space_flag:
                self.show_message_space(req_space)
        else:
            self.show_message_not_found('Cellular Layout')
        return -1, -1        

    def show_message_funds(self, cost):
        """displays a messagebox. takes cost"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Insufficient Funds!")
        msg.setInformativeText(f'Unfortunately we can not afford this now. We need {cost:,}€.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def show_message_space(self, space):
        """displays a messagebox. takes space"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Not enough space!")
        msg.setInformativeText(f'Unfortunately our building is to small. We need {space:,}m\u00b2.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def show_message_not_found(self, text):
        """displays a messagebox. takes a string"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Error 404 - Not Found!")
        msg.setInformativeText(f'Strange! Apparently there is no such thing as a {text}.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def load_layout_pictures(self):
        names = ['Fixed_Position_Layout', 'Process_Layout', 'Cellular_Layout', 'Line_Layout']
        for i in range(len(names)):
            img = QImage(f'Ressources\Images\{names[i]}.png')
            pixmap = QPixmap(img)
            label = getattr(self._panel_factory, f'lbl_tab{i + 2}_top')
            label.setPixmap(pixmap)
